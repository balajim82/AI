import fitz, requests, os

PDF_URL = "https://www.usda.gov/oce/commodity/wasde/wasde0326.pdf"


def download_pdf(path="data/wasde.pdf"):
    try:
        os.makedirs("data", exist_ok=True)
        r = requests.get(PDF_URL)
        r.raise_for_status()
        with open(path, "wb") as f:
            f.write(r.content)
        return path
    except Exception as e:
        print("[ingestion] failed to download PDF:", e)
        raise


def extract_text(path):
    try:
        doc = fitz.open(path)
        return "".join([p.get_text() for p in doc])
    except Exception as e:
        print("[ingestion] failed to extract text:", e)
        raise
