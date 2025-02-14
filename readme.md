# 📚 RAG-Based Scientific Chatbot

🚀 **Retrieval-Augmented Generation (RAG) Chatbot** designed to assist **scientific researchers** by providing **real-time AI-driven responses**. The chatbot retrieves **scientific papers** using **Elasticsearch** and generates intelligent responses using **TensorFlow-based NLP**.

## **🛠 Tech Stack**
- **Backend:** FastAPI (Python)
- **AI/ML:** TensorFlow (NLP Processing)
- **Database & Search Engine:** Elasticsearch (for Document Retrieval)
- **Frontend:** React (for Chatbot UI)
- **Version Control:** GitHub

---

## **📌 Features**
✅ **Retrieves research papers** from an indexed Elasticsearch database.  
✅ **Processes natural language queries** using a TensorFlow NLP model.  
✅ **Returns AI-generated insights** for faster research.  
✅ **Optimized search using TF-IDF, BM25, and vector embeddings.**  
✅ **FastAPI-powered REST API** for scalable interactions.  

---

## **📂 Project Structure**

```
RAG-Chatbot/
│── backend/                # FastAPI Server
│   ├── main.py             # Main FastAPI app
│   ├── index_data.py       # Script to index research papers
│   ├── requirements.txt    # Backend dependencies
│── frontend/               # React Chatbot UI
│   ├── src/                # React source files
│   ├── App.js              # Main React component
│   ├── package.json        # Frontend dependencies
│── README.md               # Project documentation
│── .gitignore              # Ignored files for GitHub
│── dataset/                # (Optional) Research Papers Dataset
```

---
## **🚀 Installation Guide (macOS)**

### **1️⃣ Prerequisites**
Ensure you have the following installed:
- **Python 3.9+** → `brew install python`
- **Node.js (for frontend)** → `brew install node`
- **Elasticsearch 7.17.4** → `brew install elastic/tap/elasticsearch-full`
- **Git (for version control)** → `brew install git`
- **Java 11 (for Elasticsearch)** → `brew install openjdk@11`

---
### **2️⃣ Clone Repository & Setup Git**
```sh
git clone https://github.com/YOUR_GITHUB_USERNAME/RAG-Chatbot.git
cd RAG-Chatbot
```

---
