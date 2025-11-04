from typing import List

def chunk_text(text: str, chunk_size: int = 500, overlap: int = 100) -> List[str]:
    """Splits text into overlapping chunks."""
    words = text.split()
    chunks = []
    start = 0
    while start < len(words):
        end = start + chunk_size
        chunk = " ".join(words[start:end])
        chunks.append(chunk)
        start += chunk_size - overlap
    return chunks

if __name__ == "__main__":
    from ingest.pdf_loader import extract_text_from_pdf
    text = extract_text_from_pdf("data/pdfs/sample.pdf")
    chunks = chunk_text(text)
    print(f"Generated {len(chunks)} chunks")
