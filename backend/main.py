from fastapi import FastAPI, Query
from elasticsearch import Elasticsearch
import tensorflow as tf
import requests

app = FastAPI()

# Initialize Elasticsearch
es = Elasticsearch("http://localhost:9200")

try:
    model = tf.keras.models.load_model("nlp_model")  # Check if it's in .keras or .h5
except ValueError:
    model = tf.keras.layers.TFSMLayer("nlp_model", call_endpoint="serving_default")


@app.get("/")
def home():
    return {"message": "RAG Chatbot API"}

@app.get("/search")
def search(query: str = Query(..., description="User research query")):
    search_body = {"query": {"match": {"content": query}}}
    results = es.search(index="scientific_papers", body=search_body)
    docs = [hit["_source"]["content"] for hit in results["hits"]["hits"]]

    # Generate AI-based response
    response = model.predict([query])  # Replace with actual inference

    return {"documents": docs, "generated_response": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

