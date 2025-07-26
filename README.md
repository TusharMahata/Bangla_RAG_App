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
bash:
python -m venv venv
bash:
source venv/bin/activate
bash:
pip install -r requirements.txt
3. 📦 Pull LLM Model via Ollama
Install Ollama and run:
bash:
ollama pull mistral
bash:
ollama run mistral
5. Start the FastAPI Server
bash:
uvicorn main:app --reload


