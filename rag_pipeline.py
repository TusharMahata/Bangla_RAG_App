from qdrant_client import QdrantClient
from qdrant_client.http.models import Filter, FieldCondition, MatchValue
from sentence_transformers import SentenceTransformer
import requests
import os

# Load embedding model (same one you used in Colab)
embed_model = SentenceTransformer('distiluse-base-multilingual-cased-v2')

# Connect to Qdrant (Cloud)

#qdrant = QdrantClient(
    #url=os.getenv("https://23ddb861-71c9-4ad6-8963-76824afc0fca.us-east4-0.gcp.cloud.qdrant.io"),
    #api_key=os.getenv("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.bBgJraK5Q5DY9U7D0_n-orcjGrEupfr01A4NeQRnfbU")
#)
qdrant = QdrantClient(
    url="https://23ddb861-71c9-4ad6-8963-76824afc0fca.us-east4-0.gcp.cloud.qdrant.io",
    api_key="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2Nlc3MiOiJtIn0.bBgJraK5Q5DY9U7D0_n-orcjGrEupfr01A4NeQRnfbU"
)

collection_name = "bangla-rag-db"

def retrieve_context(query, k=3):
    query_vec = embed_model.encode(query).tolist()
    search_result = qdrant.search(
        collection_name=collection_name,
        query_vector=query_vec,
        limit=k
    )
    return [hit.payload['text'] for hit in search_result]

def generate_answer(query, context_chunks):
    import json

    context = "\n".join(context_chunks)
    prompt = f"""Answer the following question in Bangla based only on the context:\n\nContext:\n{context}\n\nQuestion: {query}\nAnswer:"""

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "mistral", "prompt": prompt, "stream": False},  # disable streaming
            timeout=3000
        )
        response.raise_for_status()

        data = response.json()
        return data.get("response", "").strip()

    except requests.exceptions.RequestException as e:
        return f"❌ Request failed: {e}"
    except json.JSONDecodeError:
        return f"❌ Could not decode response. Raw text:\n{response.text}"


def retrieve_answer(query):
    context_chunks = retrieve_context(query)
    return generate_answer(query, context_chunks)