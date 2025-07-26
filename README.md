# Bangla_RAG_App
# Documentation and Q&A
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

Go to http://127.0.0.1:8000/docs#
POST /query
Send a JSON request:

json
{
  "question": "অনুপমের ভাষায় সুপুরুষ কাকে বলা হয়েছে?"
}
Response:

json
{
  "answer": "এই গল্পে শস্তুনাথবাবু (Baba) একটি সুপুরুষ ব্যক্ত হয়েছে।"
}




#Q&A


What method or library did you use to extract the text, and why? Did you face any formatting challenges with the PDF content?
Yes, I have faced challenges with extracting text. It was a unicode related issue. Then   I used pdf2image to convert the PDF pages into images and then pytesseract to perform Optical Character Recognition (OCR) on those images. pytesseract is a Python wrapper for Google's Tesseract-OCR Engine, which I installed along with the Bengali language pack (tesseract-ocr-ben) to handle the Bengali text in your PDF.
As for formatting challenges, OCR can sometimes introduce errors or inconsistent spacing. To address this, I implemented the clean_bangla_ocr_text function to:
Normalize line breaks.
Remove multiple consecutive spaces.
Remove non-Bengali and non-punctuation characters that might be misidentified by OCR.
Strip leading/trailing whitespace.
This cleaning step helps to standardize the text and improve the quality of the chunks for embedding.



What chunking strategy did you choose (e.g. paragraph-based, sentence-based, character limit)? Why do you think it works well for semantic retrieval?
I used a chunking strategy based on a character limit with overlap, while also trying to prioritize sentence boundaries for cleaner chunks.
The chunk_text_bangla function works as follows:
It iterates through the text based on a chunk_size (defaulting to 500 characters).
If a chunk boundary falls mid-sentence, it attempts to find the nearest sentence-ending punctuation (।, !, ?) within the potential chunk to make the break there instead. This helps to keep complete sentences within a single chunk, which is generally better for maintaining semantic meaning.
An overlap (defaulting to 100 characters) is included between consecutive chunks. This overlap ensures that if a relevant piece of information spans across a chunk boundary, it will still be present in the overlapping portion of the next chunk, reducing the chance of missing context during retrieval.
This strategy works well for semantic retrieval because:
Sentence Integrity: By trying to chunk at sentence boundaries, we keep complete thoughts or ideas together, which is crucial for embeddings to capture the full meaning.
Context Preservation: The overlap helps to maintain context between chunks, allowing the embedding model to better understand the relationship between adjacent pieces of text.
Manageable Size: The character limit keeps the chunks to a reasonable size, preventing overly long chunks that might dilute the semantic focus or exceed the input limits of some embedding models or language models.
Overall, this approach aims to create chunks that are semantically coherent and contain sufficient context for effective retrieval based on user queries.


What embedding model did you use? Why did you choose it? How does it capture the meaning of the text?
I used the distiluse-base-multilingual-cased-v2 embedding model. I chose it because it supports Bangla and other languages with strong semantic understanding. It is based on a distilled multilingual BERT and trained using contrastive learning. The model encodes text into dense vector representations that preserve meaning. These vectors enable similarity-based search for relevant context in Qdrant.


How are you comparing the query with your stored chunks? Why did you choose this similarity method and storage setup?

I’m using semantic similarity via dense vector embeddings and comparing them using vector search powered by Qdrant.
Qdrant uses cosine similarity (by default) to compare the query vector with stored vectors.
This retrieves the chunks semantically closest to your question, not just keyword matches.

This method and storage setup gives flexibility for Handle Synonyms, to work across languages, context understanding, Optimized for high-performance vector search, Easy to use Python SDK, Cloud-hosted version simplifies deployment, Supports filters, payloads, metadata storage





How do you ensure that the question and the document chunks are compared meaningfully? What would happen if the query is vague or missing context?

To meaningfully compare the user’s question with stored document chunks, my system uses semantic embeddings and vector similarity search. 
if the query is vague or missing context, it will return low-similarity chunks or nothing useful or less relevant or inaccurate response. 



Do the results seem relevant? If not, what might improve them (e.g. better chunking, better embedding model, larger document)?
Yes, its giving relevant output. But if I want to improve this, I can do following way-
Chunking:
Avoid cutting mid-thought/context loss
Sentence-based or token-aware chunking
Embedding Model:
Bge-m3, fine-tuned SBERT etc. 
Document:
Expand corpus, clean/preprocess documents.
Prompt Engineering:
Add fallback instructions, clarify tone.

