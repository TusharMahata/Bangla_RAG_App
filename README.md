# Bangla_RAG_App
Technologies Used
Component	Technology
Embeddings	distiluse-base-multilingual-cased-v2 (supports Bangla)
Vector DB	Qdrant Cloud
LLM (local)	Ollama with mistral
Backend API	FastAPI
Language Support	🟢 Bangla

🚀 Setup Instructions
1. 🔧 Install Dependencies
bash
Copy
Edit
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
2. 📦 Pull LLM Model via Ollama
Install Ollama and run:
cmd:ollama pull mistral 
cmd:ollama run mistral
3. Start the FastAPI Server 
cmd: uvicorn main:app --reload
