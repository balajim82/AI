from abc import ABC, abstractmethod


class BaseWorker(ABC):

    @abstractmethod
    async def execute(self, data: dict):
        pass
