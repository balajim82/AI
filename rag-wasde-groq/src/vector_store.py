import lancedb
import pandas as pd
import pyarrow as pa
import os

DB_PATH = "lancedb"


def connect_db():
    try:
        os.makedirs(DB_PATH, exist_ok=True)
        return lancedb.connect(DB_PATH)
    except Exception as e:
        print("[vector_store] failed to connect to DB:", e)
        raise


def create_table(db, embedding_dim: int):
    """Create or overwrite the LanceDB table with a proper vector column schema."""

    try:
        schema = pa.schema(
            [
                ("text", pa.string()),
                ("vector", lancedb.vector(dimension=embedding_dim)),
                ("commodity", pa.string()),
                ("country", pa.string()),
            ]
        )

        return db.create_table("WASDE_REPROT_TABLE", schema=schema, mode="overwrite")
    except Exception as e:
        print("[vector_store] failed to create table:", e)
        raise


def insert_data(table, texts, embeddings, metadata):
    try:
        rows = []
        for i in range(len(texts)):
            rows.append(
                {
                    "text": texts[i],
                    "vector": embeddings[i],
                    "commodity": metadata[i]["commodity"],
                    "country": metadata[i]["country"],
                }
            )
        table.add(pd.DataFrame(rows))
    except Exception as e:
        print("[vector_store] failed to insert data:", e)
        raise
