from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

try:
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
except Exception as e:
    print("[rag_pipeline] failed to init Groq client:", e)
    client = None


def generate_answer(context, query):
    if client is None:
        raise RuntimeError("Groq client is not initialized")

    try:
        prompt = f"Context:\n{context}\n\nQuestion:{query}"
        res = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
        )
        return res.choices[0].message.content
    except Exception as e:
        print("[rag_pipeline] failed to generate answer:", e)
        raise
