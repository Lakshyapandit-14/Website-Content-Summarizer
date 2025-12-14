from bs4 import BeautifulSoup

def extract_main_text(html: str) -> str:
    """Very simple extractor: gets article-like sections and joins paragraphs.
    For production consider readability-lxml, newspaper3k, or boilerpipe.
    """
    soup = BeautifulSoup(html, "lxml")

    # remove scripts/styles
    for s in soup(["script", "style", "noscript", "header", "footer", "svg"]):
        s.decompose()

    # try common article containers
    selectors = ["article", "main", "#content", ".post", ".article"]
    parts = []
    for sel in selectors:
        node = soup.select_one(sel)
        if node:
            parts.append("\n".join(p.get_text(strip=True) for p in node.find_all("p")))
    if not parts:
        # fallback: all paragraphs
        parts.append("\n".join(p.get_text(strip=True) for p in soup.find_all("p")))

    text = "\n\n".join([p for p in parts if p.strip()])
    return text
