import asyncio
import os
from src.workers.base_worker import BaseWorker
from src.utils.logger import get_logger

logger = get_logger(__name__)


class AsyncWorker(BaseWorker):

    async def execute(self, n: int):
        print(f"Task started in PID {os.getpid()} for {n}")
        logger.info(f"Started AsyncWorker processing {n}")
        await asyncio.sleep(2)  # non-blocking

        print(f"Task finished in PID {os.getpid()} for {n}")
        logger.info(f"End AsyncWorker processing {n}")
        return {"input": n, "pid": os.getpid()}
