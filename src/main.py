from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, HttpUrl
import asyncio
from .agent.summarizer_agent import WebsiteSummarizerAgent
from .config import DEFAULT_BACKEND

app = FastAPI(title="LangGraph Website Summarizer")

class SummarizeRequest(BaseModel):
    url: HttpUrl
    backend: str | None = None
    max_chunk_chars: int | None = 2000

class SummarizeResponse(BaseModel):
    url: HttpUrl
    num_chunks: int
    summary: str

@app.post("/summarize", response_model=SummarizeResponse)
async def summarize(req: SummarizeRequest):
    agent = WebsiteSummarizerAgent(backend=req.backend or DEFAULT_BACKEND)
    res = await agent.run(str(req.url), max_chunk_chars=800)   # <= FIX

    if "error" in res:
        raise HTTPException(status_code=400, detail=res["error"])
    return res

@app.get("/")
async def root():
    return {"msg": "LangGraph Website Summarizer is running"}
