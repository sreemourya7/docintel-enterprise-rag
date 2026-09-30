from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="DocIntel API",
    description="Enterprise document intelligence and RAG API",
    version="0.1.0",
)


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def root():
    return {
        "project": "DocIntel",
        "status": "development",
        "message": "Enterprise RAG and document intelligence platform",
    }


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/ask")
def ask_question(request: QuestionRequest):
    # Retrieval + citation pipeline will be connected here.
    return {
        "question": request.question,
        "answer": "RAG pipeline is currently under development.",
        "citations": [],
    }
