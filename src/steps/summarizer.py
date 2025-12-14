from typing import Optional, List
from ..config import DEFAULT_BACKEND, HF_MODEL, HF_MAX_TOKENS, OPENAI_API_KEY

class Summarizer:
    def __init__(self, backend: Optional[str] = None):
        self.backend = backend or DEFAULT_BACKEND
        if self.backend == "openai":
            try:
                import openai
                openai.api_key = OPENAI_API_KEY
                self.openai = openai
            except Exception as e:
                raise RuntimeError("OpenAI selected but openai is not installed or key missing")
        else:
            # HF pipeline lazy init
            from transformers import pipeline
            self.pipe = pipeline("summarization", model=HF_MODEL)

    def summarize_chunk(self, text: str, max_length: int = HF_MAX_TOKENS) -> str:
        if self.backend == "openai":
            resp = self.openai.ChatCompletion.create(
                model="gpt-4o-mini" if hasattr(self.openai, "ChatCompletion") else "gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful summarization assistant."},
                    {"role": "user", "content": f"Summarize the following content in 2-4 sentences:\n\n{text}"},
                ],
                max_tokens=max_length,
                temperature=0.0,
            )
            try:
                return resp.choices[0].message.content.strip()
            except Exception:
                return resp["choices"][0]["message"]["content"].strip()
        else:
            out = self.pipe(text, max_length=max_length, min_length=30)[0]
            return out["summary_text"].strip()

    def summarize(self, chunks: List[str], max_length_per_chunk: int = HF_MAX_TOKENS) -> str:
        summaries = [self.summarize_chunk(c, max_length_per_chunk) for c in chunks]
        combined = "\n\n".join(summaries)

        if self.backend == "openai":
            resp = self.openai.ChatCompletion.create(
                model="gpt-4o-mini" if hasattr(self.openai, "ChatCompletion") else "gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful summarization assistant."},
                    {"role": "user", "content": f"Given the following chunk-level summaries, produce a short (3-5 sentence) cohesive summary:\n\n{combined}"},
                ],
                max_tokens=HF_MAX_TOKENS,
                temperature=0.0,
            )
            try:
                return resp.choices[0].message.content.strip()
            except Exception:
                return resp["choices"][0]["message"]["content"].strip()
        else:
            out = self.pipe(combined, max_length=HF_MAX_TOKENS, min_length=40)[0]
            return out["summary_text"].strip()
