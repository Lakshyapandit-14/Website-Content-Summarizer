from ..steps.fetcher import fetch_url
from ..steps.parser import extract_main_text
from ..steps.splitter import chunk_text
from ..steps.summarizer import Summarizer
from .graph import Graph, Node
from typing import Dict, Any

class WebsiteSummarizerAgent:
    def __init__(self, backend: str = None):
        self.summarizer = Summarizer(backend=backend)

    async def run(self, url: str, max_chunk_chars: int = 2000) -> Dict[str, Any]:
        html = await fetch_url(url)
        if not html:
            return {"error": "failed to fetch URL"}
        text = extract_main_text(html)
        if not text.strip():
            return {"error": "no extractable text"}
        chunks = chunk_text(text, chunk_size=max_chunk_chars)

        summary = self.summarizer.summarize(chunks)
        return {
            "url": url,
            "num_chunks": len(chunks),
            "summary": summary,
        }
