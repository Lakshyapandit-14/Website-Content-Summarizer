from langchain_text_splitters import RecursiveCharacterTextSplitter


def chunk_text(text: str, chunk_size: int = 1200, chunk_overlap: int = 200):
    """
    Use LangChain's RecursiveCharacterTextSplitter 
    to split text into clean & safe chunks for the summarizer.
    
    chunk_size = max characters per chunk  
    chunk_overlap = to avoid losing context
    """
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ".", "?", "!", " ", ""]
    )

    chunks = splitter.split_text(text)
    return chunks
