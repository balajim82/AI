def chunk_text(text, chunk_size=500, overlap=100):
    try:
        chunks = []
        i = 0
        while i < len(text):
            chunks.append(text[i : i + chunk_size])
            i += chunk_size - overlap
        return chunks
    except Exception as e:
        print("[utils] failed to chunk text:", e)
        raise
