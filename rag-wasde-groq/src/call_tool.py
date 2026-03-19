import sys
from src.retriever import search
from src.rag_pipeline import generate_answer
from src.vector_store import connect_db
from src.ingestion import download_pdf, extract_text
from src.utils import chunk_text
from src.metadata import detect_metadata
from src.embedding import get_embeddings
from src.vector_store import connect_db, create_table, insert_data
from src.rdbs import insert_data, retrive_data
import pandas as pd


def decide_retrival_tool():
    user_question = str(input("Enter your Question: "))
    user_question = user_question.lower()
    try:
        if not user_question:
            raise ValueError("User Input should not empty")
        else:
            if any(
                word in user_question
                for word in ["database", "sql", "db", "select", "fetech"]
            ):
                call_retrival_sql_tool(user_question)
            else:
                call_retrival_rag_tool(user_question)
    except Exception as e:
        print("[app] call_retrival_sql_tool failed:", e)


def call_vector_ingestion_tool():
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


def call_retrival_rag_tool(query):
    try:
        if not query:
            raise ValueError("Query prompt cannot be empty")
        else:
            db = connect_db()
            table = db.open_table("WASDE_REPROT_TABLE")
            results = search(table, query, commodity="Wheat", country="USA")
            context = "\n\n".join(results["text"].tolist())
            answer = generate_answer(context, query)
            print(answer)
    except Exception as e:
        print("[app] call_retrival_rag_tool failed:", e)
        sys.exit(1)


def decide_ingenstion_tool():
    user_input = str(input("Please confirm which DB you want to ingenstion (R/V) "))
    try:
        if not user_input:
            raise ValueError("User Input should not empty")
        else:
            if "R" == user_input:
                call_relation_ingestion_tool()
            elif "V" == user_input:
                call_vector_ingestion_tool()
    except Exception as e:
        print("[app] decide_ingenstion_tool failed:", e)


def call_relation_ingestion_tool():
    try:
        df = prepare_data()
        insert_data(df)
    except Exception as e:
        print("[app] call_relation_ingestion_tool failed:", e)


def prepare_data():
    try:
        data = {
            "commodity": ["Wheat", "Corn", "Cotton"],
            "country": ["USA", "India", "Brazil"],
            "wr_description": [
                "Wheat production increased",
                "Corn demand stable",
                "Cotton export high",
            ],
        }
        df = pd.DataFrame(data)
    except Exception as e:
        print(" Preparing data Frame ")
    return df


def call_retrival_sql_tool(query):
    try:
        print("WASDE Report Dashboard")
        print("### Data from MySQL Table")
        df = retrive_data()
        # Display table
        print(df)
        # Optional: show row count
        print(f"Total Records: {len(df)}")

    except Exception as e:
        print("[app] call_retrival_sql_tool failed:", e)
        sys.exit(1)
