from concurrent.futures import ProcessPoolExecutor
import asyncio
from src.workers.base_worker import BaseWorker
import time
import os
from src.utils.logger import get_logger

logger = get_logger(__name__)


def heavy_task(n: int):
    print(f"Process {os.getpid()} started for input {n}", flush=True)
    logger.info(f"Started ProcessWorker processing in heavy_task method for {n}")
    total = 0
    for i in range(10_000_000):
        total += i * n

    time.sleep(2)  # simulate delay
    logger.info(f"Started ProcessWorker processing in heavy_task method for {n}")
    print(f"Process {os.getpid()} finished for input {n}", flush=True)
    return {"input": n, "resultd": total, "pid": os.getpid()}


class ProcessWorker(BaseWorker):
    logger.info(f"Started ProcessWorker processing Init method")

    def __init__(self):
        self.executor = ProcessPoolExecutor(max_workers=4)

    async def execute(self, n: int):
        logger.info(f"Started ProcessWorker executemethod")
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(self.executor, heavy_task, n)
