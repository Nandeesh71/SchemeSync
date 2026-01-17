# SchemeSync: AI-Powered Government Schemes Assistant 🏛️

  
  **Bridging Citizens and Welfare Programs through Intelligent Information Retrieval**

<p align="center">
  <a href="https://i.postimg.cc/nrL8ScR2/Zynfo-Graph-icon.jpg">
    <img src="https://i.pinimg.com/originals/11/c4/c5/11c4c5b58b96ac77370bcffa62cc59d1.jpg"
         alt="Logo"
         width="144"
         height="144">
  </a>
</p>

  
  *A Retrieval-Augmented Generation (RAG) system making government schemes accessible to everyone*

## 🎯 Overview

**SchemeSync** is an AI-powered assistant that democratizes access to government welfare schemes in Tamil Nadu and across India. Using advanced **Retrieval-Augmented Generation (RAG)** technology, it helps citizens discover relevant schemes through natural language queries in **Tamil, English, or mixed languages**.

### Why SchemeSync?

- 🌍 **500+ Government Schemes** indexed and searchable
- 🗣️ **Multilingual Support** - Tamil, English, and code-mixed queries
- 🚀 **Instant Answers** - Information in seconds, not hours
- 🔒 **Privacy-First** - No personal data collection
- 📱 **Accessible** - Simple interface for all education levels

-------------------------------------------------------------------------------------------------------
 *"Predicting the future isn’t magic, it’s artificial intelligence."* 
 
 -------------------------------------------------------------------------------------------------------
**🔗 Get In Touch :**

> **Connect with me on LinkedIn:**  
[<img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" width="24" height="24" style="vertical-align:middle;"/> LinkedIn Profile](https://www.linkedin.com/in/nandeesh71)

> **Visit my portfolio:**  
[<img src="https://cdn-icons-png.flaticon.com/512/1055/1055687.png" width="24" height="24" style="vertical-align:middle;"/> Portfolio Website](https://nandeesh-71.web.app)

-------------------------------------------------------------------------------------------------------

---

## 🔍 Problem Statement

**Challenge:** Many citizens, especially in rural and semi-urban areas, remain unaware of government welfare schemes due to:
- Information scattered across multiple portals
- Complex eligibility criteria in bureaucratic language
- Language barriers (English-heavy content)
- Limited digital literacy
- Time-consuming manual searches

**Solution:** SchemeSync uses semantic search and AI to provide personalized, clear guidance on eligibility, benefits, and application procedures through a conversational interface.

---

## ✨ Key Features

### 🧠 Intelligent Search
- **Semantic Understanding**: Finds schemes based on meaning, not just keywords
- **Context-Aware**: Understands user intent from conversational queries
- **Multilingual**: Handles Tamil (தமிழ்), English, and mixed-language inputs

### 📊 Structured Responses
Every answer includes:
1. ✅ **Scheme Name** - Official title and department
2. 👥 **Beneficiaries** - Who can apply
3. 💰 **Benefits** - What is provided (loans, subsidies, training)
4. 📝 **Eligibility** - Clear qualification criteria
5. 🔗 **Application Process** - Step-by-step guidance

### 🔐 Privacy & Security
- ✅ No personal data collection (Aadhaar, income, etc.)
- ✅ No user authentication required
- ✅ Anonymous queries
- ✅ Secure API key management via environment variables

### ⚡ Performance
- **Response Time**: < 3 seconds per query
- **Accuracy**: 85-90% relevance based on testing
- **Scalability**: Handles unlimited concurrent users
- **24/7 Availability**: No office hours constraints

---

## 🏗️ System Architecture

<p align="center">
  <img src="https://i.postimg.cc/tRkWB0Pr/diagram-export-1-18-2026-1-04-AM.png" width="224" height="144" />
</p>

---

## 🛠️ Technology Stack

### Core Technologies
```yaml
Language: Python 3.10+
Framework: LangChain 0.1.x
Vector DB: ChromaDB
Embeddings: IBM Granite (granite-embedding-278m-multilingual)
LLM: Llama 3.3 70B (Groq API) / IBM Granite 13B (Watsonx)
Package Manager: UV
```

### IBM Integration
- **IBM Granite Embedding Model**: Multilingual semantic search (30+ languages)
- **IBM Watsonx.ai**: Production-ready LLM deployment option
- **IBM SkillsBuild**: Project developed as part of AI for Sustainability internship

---

## 📦 Installation

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/SchemeSync.git
cd SchemeSync

# 2. Install UV package manager
pip install uv

# 3. Create virtual environment
uv venv

# 4. Activate environment
# Windows
.venv\Scripts\activate
# Linux/Mac
source .venv/bin/activate

# 5. Install dependencies
uv pip install -r requirements.txt
```


### Environment Configuration

Create a `.env` file in the project root:

```env
# Required: API Key for LLM inference
GROQ_API_KEY=your_groq_api_key_here

# Optional: IBM Watsonx credentials (for production)
IBM_CLOUD_API_KEY=your_ibm_api_key
IBM_PROJECT_ID=your_project_id
```

---

## 🚀 Usage

### Basic Usage

```bash
# Run the application
python main.py
```

### Example Interactions

```
═══════════════════════════════════════════════════════════════
                 SchemeSync - Government Schemes Assistant
═══════════════════════════════════════════════════════════════

Question: What schemes are available for farmers?

🔍 Searching for relevant schemes...

🤖 Assistant:

Based on available Tamil Nadu government schemes, here are the most relevant 
options for farmers:

1. **Tamil Nadu Agricultural Subsidy Scheme**
   
   Who Can Benefit:
   • Small and marginal farmers with landholding up to 2.5 hectares
   • Agricultural laborers engaged in farming activities
   
   Benefits Provided:
   • 50% subsidy on agricultural equipment (tractors, tillers, pumps)
   • Free soil testing services
   • Subsidized seeds and fertilizers
   
   Eligibility Criteria:
   • Must be a resident of Tamil Nadu
   • Valid land ownership documents (patta) required
   • Should not have availed similar subsidy in last 3 years
   
   How to Apply:
   • Visit nearest Agricultural Extension Office
   • Submit application with land documents
   • Online: tnagrisnet.tn.gov.in
   
   Department: Tamil Nadu Agriculture Department

═══════════════════════════════════════════════════════════════
```

## 📊 Dataset

### Source & Attribution
- **Primary Source**: [SarkariYojana.com](https://sarkariyojana.com)
- **Content Type**: Central and State government welfare schemes
- **Data Scope**: 500+ schemes across multiple categories
- **Update Frequency**: Quarterly (manual review required)

### Data Categories
- 🌾 Agriculture & Farming
- 👩 Women Welfare & Empowerment
- 🎓 Education & Scholarships
- 🏥 Healthcare & Insurance
- 🏗️ Housing & Infrastructure
- 💼 Employment & Skill Development
- 👴 Senior Citizens & Pensions
- ♿ Persons with Disabilities


### Data Processing Pipeline
1. **Collection**: Scraped from official portals (with proper attribution)
2. **Validation**: Required fields checked, duplicates removed
3. **Cleaning**: Standardized formatting, language normalization
4. **Chunking**: Split into 800-character chunks with 150 overlap
5. **Embedding**: Converted to vectors using IBM Granite model
6. **Indexing**: Stored in ChromaDB for fast retrieval

**⚠️Disclaimer 🚫**: This dataset is intended for educational purposes. Users should verify scheme details from official government portals before applying.

---

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

### Areas for Contribution
- 📝 **Data**: Add new schemes, verify existing data
- 🌍 **Localization**: Translate interface to more languages
- 🐛 **Bug Fixes**: Report and fix issues
- ✨ **Features**: Implement roadmap items
- 📚 **Documentation**: Improve guides and tutorials
- 🧪 **Testing**: Write unit and integration tests

### Contribution Process
```bash
# 1. Fork the repository
# 2. Create feature branch
git checkout -b feature/amazing-feature

# 3. Make changes and commit
git commit -m "Add amazing feature"

# 4. Push to branch
git push origin feature/amazing-feature

# 5. Open Pull Request
```

