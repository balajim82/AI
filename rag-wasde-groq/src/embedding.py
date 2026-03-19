from sentence_transformers import SentenceTransformer
from transformers import logging
from huggingface_hub.utils import logging as hf_logging
import warnings


def _load_model():
    try:
        logging.set_verbosity_error()
        hf_logging.set_verbosity_error()
        warnings.filterwarnings("ignore", message=".*position_ids.*")
        return SentenceTransformer("all-MiniLM-L6-v2")
    except Exception as e:
        # Fail fast with a clear message; calling code can decide how to handle it.
        print("[embedding] failed to load SentenceTransformer model:", e)
        return None


_model = _load_model()


def get_embeddings(texts):
    """Return embedding vectors for a list of texts.

    Args:
        texts: A list of strings to embed.

    Returns:
        A list of float vectors (list of lists).

    Raises:
        RuntimeError: If the embedding model is not loaded or encoding fails.
    """

    try:
        if _model is None:
            raise RuntimeError("Embedding model is not loaded")
        return _model.encode(texts).tolist()
    except Exception as e:
        print("[embedding] failed to compute embeddings:", e)
        raise
