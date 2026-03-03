# AI & Digital Economy FAQ Chatbot (Team E)

##  Project Objective
This project is a domain-specific AI assistant developed by **Team E**. It is designed to accurately answer predefined questions related to Artificial Intelligence and the Digital Economy using retrieval-based methods.

## Team Members:
Kong Chuinan
Yan Jiajie

##  Key Features
**Retrieval-Based Answering:** Utilizes Natural Language Processing (NLP) to match user queries with a structured knowledge base.
**Advanced Text Embeddings:** Powered by `sentence-transformers` for high-accuracy semantic matching, bypassing rigid keyword searches.
- **Cosine Similarity Search:** Computes the mathematical distance between user queries and stored FAQs to find the most relevant answer.
- **Confidence Scoring:** Every response is accompanied by a transparent confidence score (percentage) and topic categorization.
- **Architecture Decoupling:** Strict separation between the interactive UI (`search.py`), the core retrieval engine (`engine.py`), and the knowledge base (`faq_data.json`).
- ** Bonus: Multilingual Support:** Automatically detects user language and seamlessly provides answers in **English, Russian (Русский), and Uzbek (O'zbekcha)**.

##  Technical Stack
- **Frontend / UI:** Streamlit (Web interface)
- **Core Engine:** Python
- **Vector Embeddings:** `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`
- **Similarity Computation:** `scikit-learn` (Cosine Similarity)
- **Language Detection:** `langdetect`
- **Data Storage:** In-memory vector storage (loaded from structured JSON)

##  Project Structure

ai_assistant/
│
├── data/son      # Structured Knowledge Base (20+ Multilingual Q&As)
│
├── engine.py              # Core logic: Embeddings, similarity search, & language detection
├── search.py              # Web Interface (Streamlit application)
└── README.md              # Project documentation
 Installation Instructions

1. Clone the repository
Bash
git clone [https://github.com/y1479642282-cmd/ai_assistant.git](https://github.com/y1479642282-cmd/ai_assistant.git)
cd ai_assistant

2.INSTALL
   pip install streamlit sentence-transformers scikit-learn langdetect
   Usage Instructions
To launch the AI chatbot web interface, run the following command in your terminal from the root directory of the project:

3.RUN!!!
   streamlit run search.py
Note: On the first run, the system will automatically download the multilingual embedding model (approx. 400MB). Subsequent runs will be instant.

Knowledge Base Topics Covered
Our structured database currently holds 20 core Q&As covering the following domains:
1.Smart Governance & International AI Applications
2.Data Privacy & GDPR
3.AI Adoption, NLP, & Parallel Computing
4.Digital Transformation & Cloud Computing
5.Digital Economy, Fintech & Gig Economy

