from typing import Optional
import httpx

async def fetch_url(url: str, timeout: int = 15) -> Optional[str]:
    """Fetch page HTML. Returns None on failure."""
    try:
        async with httpx.AsyncClient(timeout=timeout, follow_redirects=True) as client:
            r = await client.get(url)
            r.raise_for_status()
            return r.text
    except Exception:
        return None
