import os
import json
from typing import List, Dict
from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
from groq import Groq


# -------------------- DATA LOADER --------------------

class SchemeDataLoader:
    REQUIRED_FIELDS = [
        "name", "category", "beneficiaries", "benefits",
        "eligibility", "howToApply", "department", "description"
    ]

    @staticmethod
    def load(filepath: str) -> List[Dict]:
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)

        if not isinstance(data, list):
            raise ValueError("Schemes JSON must be a list")

        validated = []
        for scheme in data:
            item = {k: str(scheme.get(k, "")).strip() for k in SchemeDataLoader.REQUIRED_FIELDS}
            if not item["name"]:
                continue

            item["url"] = scheme.get("url", "")
            item["source"] = scheme.get("source", "Tamil Nadu Government")
            validated.append(item)

        return validated


# -------------------- RAG SYSTEM --------------------

class SchemesRAG:
    def __init__(self, persist_dir: str = "./chroma_db"):
        api_key = os.getenv("API_KEY")
        if not api_key:
            raise EnvironmentError("Set API_KEY as an environment variable")

        self.client = Groq(api_key=api_key)
        self.persist_dir = persist_dir
        self.vectorstore = None

        self.embeddings = HuggingFaceEmbeddings(
            model_name="ibm-granite/granite-embedding-278m-multilingual",
            encode_kwargs={"normalize_embeddings": True}
        )
        

    def build_vectorstore(self, schemes: List[Dict], rebuild: bool = False):
        path = Path(self.persist_dir)

        if path.exists() and not rebuild:
            self.vectorstore = Chroma(
                persist_directory=self.persist_dir,
                embedding_function=self.embeddings
            )
            return

        documents = []
        for s in schemes:
            content = (
                f"Scheme Name: {s['name']}\n"
                f"Category: {s['category']}\n"
                f"Department: {s['department']}\n\n"
                f"Beneficiaries: {s['beneficiaries']}\n\n"
                f"Benefits: {s['benefits']}\n\n"
                f"Eligibility: {s['eligibility']}\n\n"
                f"How to Apply: {s['howToApply']}\n\n"
                f"Description: {s['description']}"
            )

            documents.append(
                Document(
                    page_content=content,
                    metadata={
                        "name": s["name"],
                        "category": s["category"],
                        "department": s["department"],
                        "url": s["url"]
                    }
                )
            )

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=800,
            chunk_overlap=150
        )

        split_docs = splitter.split_documents(documents)

        self.vectorstore = Chroma.from_documents(
            split_docs,
            self.embeddings,
            persist_directory=self.persist_dir
        )

    def answer(self, query: str, k: int = 5) -> str:
        if not self.vectorstore:
            raise RuntimeError("Vector store not initialized")

        docs = self.vectorstore.similarity_search(query, k=k)
        if not docs:
            return "I could not find relevant information for this query."

        context = "\n\n".join(d.page_content for d in docs)

        prompt = f"""
You are an assistant explaining Government schemes espically for Tamil Nadu Government.

Rules:
- Use only the provided context
- Be clear, polite, and factual
- Do not add assumptions

Context:
{context}

Question:
{query}

Answer:

Provide a clear answer including:
1. Most relevant scheme(s)
2. Who can benefit
3. What benefits are provided
4. How to apply
5. Eligibility criteria

Use simple, encouraging language.
"""

        response = self.client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You provide accurate government scheme information."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            top_p=0.8,
            max_tokens=900
        )

        return response.choices[0].message.content.strip()


# -------------------- MAIN --------------------

def main():
    schemes = SchemeDataLoader.load("schemes.json")

    rag = SchemesRAG()
    rag.build_vectorstore(schemes)
    
    print('\n')
    print("=-="*67)
    print("\n\t\t\t\t\t\t\t\t\t SCHEMESYNC: AI-POWERED GOVERNMENT SCHEMES ASSISTANT  \n")
    print("\t\t\t\t\t\t\t\t Empowering citizens with accurate and accessible scheme information\n")

    print("=-="*67)
    
    print("\nWelcome to SchemeSync.")
    print("You may ask questions related to government welfare schemes, eligibility, benefits, and application procedures\n")
    
    while True:
        q = input("\nQuestion: ").strip()
        if q.lower() in {"exit", "quit"}:
            break
        print("\n🔍 Searching for relevant schemes...")
        print("\n🤖 Assistant:\n")
        print("\n" + rag.answer(q))
        print('\n')
        print("=-="*67)


if __name__ == "__main__":
    main()
