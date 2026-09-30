# DocIntel

Production-style enterprise document intelligence platform for retrieval-augmented generation (RAG), citation-grounded question answering, and document evaluation.

## Why this project

DocIntel is designed to explore the engineering challenges behind enterprise AI systems:

- Document ingestion and chunking
- Semantic retrieval and reranking
- Citation-grounded LLM responses
- Role-aware document access
- RAG evaluation and regression testing
- Production API deployment

## Current status

Starter API is implemented with FastAPI. Retrieval, embeddings, evaluation, and document ingestion are being added incrementally.

## Tech stack

- Python
- FastAPI
- PyTorch / Hugging Face
- pgvector or FAISS
- Docker
- pytest
- GitHub Actions

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
# .venv\Scripts\activate  # Windows

pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open:

`http://127.0.0.1:8000/docs`

## API

### Health check

`GET /health`

### Ask a question

`POST /ask`

Example request:

```json
{
  "question": "What is the termination clause?"
}
```

The current endpoint returns a placeholder response while the retrieval pipeline is under development.

## Planned milestones

1. Document ingestion and chunking
2. Hugging Face embeddings
3. Vector retrieval with pgvector / FAISS
4. Hybrid retrieval and reranking
5. Citation-grounded generation
6. Evaluation suite for Recall@K, citation accuracy, groundedness, and latency
7. Docker deployment and CI regression tests

## Planned evaluation

The final system will compare:

- Dense vector retrieval
- Hybrid BM25 + dense retrieval
- Hybrid retrieval + cross-encoder reranking

Metrics will be reported only after reproducible evaluation runs are completed.
