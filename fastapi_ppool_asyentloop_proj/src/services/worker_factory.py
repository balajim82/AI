from src.core.config import settings
from src.workers.process_worker import ProcessWorker
from src.workers.async_worker import AsyncWorker
from src.utils.logger import get_logger

logger = get_logger(__name__)


def get_worker():
    logger.info(f"Start worker_factory file, get_worker Method")
    if settings.WORKER_MODE == "async":
        return AsyncWorker()
    return ProcessWorker()
