from src.embedding import get_embeddings


def search(table, query, commodity=None, country=None, top_k=5):
    try:
        emb = get_embeddings([query])[0]
        df = table.search(emb).limit(10).to_pandas()

        if commodity:
            df = df[df["commodity"].apply(lambda x: commodity in x)]
        if country:
            df = df[df["country"].apply(lambda x: country in x)]

        return df.head(top_k)
    except Exception as e:
        print("[retriever] failed to search:", e)
        raise
