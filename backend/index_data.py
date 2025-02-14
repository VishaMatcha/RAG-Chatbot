from elasticsearch import Elasticsearch
import json

es = Elasticsearch("http://localhost:9200")

# Sample dataset
documents = [
    {"title": "Deep Learning for NLP", "content": "Deep learning has revolutionized NLP..."},
    {"title": "Transformers in Research", "content": "The transformer model is widely used..."},
]

# Create Index
es.indices.create(index="scientific_papers", ignore=400)

# Index Documents
for doc in documents:
    es.index(index="scientific_papers", document=doc)

print("Data indexed successfully.")


