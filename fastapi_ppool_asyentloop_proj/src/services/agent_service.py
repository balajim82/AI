from src.services.worker_factory import get_worker
from src.utils.logger import get_logger

logger = get_logger(__name__)


class AgentService:
    logger.info(f"Start AgentService initialization")

    def __init__(self):
        self.worker = get_worker()

    async def invoke(self, n: int):
        logger.info(f"Start AgentService invoke Method")
        return await self.worker.execute(n)
