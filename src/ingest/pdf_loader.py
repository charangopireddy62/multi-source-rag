import pdfplumber
from pathlib import Path

def extract_text_from_pdf(pdf_path: str) -> str:
    """Extracts raw text from a PDF file."""
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text.strip()

if __name__ == "__main__":
    sample_pdf = Path("data/pdfs/sample.pdf")
    print(extract_text_from_pdf(sample_pdf))
