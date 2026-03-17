import sys

from src.ingestion import download_pdf, extract_text
from src.utils import chunk_text
from src.metadata import detect_metadata
from src.embedding import get_embeddings
from src.vector_store import connect_db, create_table, insert_data
from src.retriever import search
from src.rag_pipeline import generate_answer


def run_ingestion():
    try:
        pdf_path = download_pdf()
        text = extract_text(pdf_path)
        chunks = chunk_text(text)
        metadata_list = [detect_metadata(c) for c in chunks]
        embeddings = get_embeddings(chunks)

        db = connect_db()
        embedding_dim = (
            len(embeddings[0]) if len(embeddings) and embeddings[0] is not None else 0
        )
        table = create_table(db, embedding_dim=embedding_dim)
        insert_data(table, chunks, embeddings, metadata_list)
        print("Ingestion Complete")
    except Exception as e:
        print("[app] ingestion failed:", e)
        raise


def run_query():
    try:
        db = connect_db()
        table = db.open_table("wasde")
        query = input("Enter your question: ").strip()
        if not query:
            raise ValueError("Query prompt cannot be empty")
        else:
            results = search(table, query, commodity="Wheat", country="USA")
            context = "\n\n".join(results["text"].tolist())
            answer = generate_answer(context, query)
            print(answer)
    except Exception as e:
        print("[app] query failed:", e)
        sys.exit(1)
        raise


if __name__ == "__main__":
    run_ingestion()
    run_query()
