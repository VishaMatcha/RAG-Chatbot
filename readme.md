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
