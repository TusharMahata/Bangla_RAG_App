from fastapi import FastAPI
from pydantic import BaseModel
from rag_pipeline import retrieve_answer

app = FastAPI()

# Define Pydantic model for input
class QueryRequest(BaseModel):
    question: str

# Root health check
@app.get("/")
def home():
    return {"status": "RAG system running."}

# Query endpoint with JSON body
@app.post("/query")
def ask(payload: QueryRequest):
    answer = retrieve_answer(payload.question)
    return {"answer": answer}
