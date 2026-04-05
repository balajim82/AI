from fastapi import APIRouter
from src.models.request_model import ProcessRequest
from src.services.agent_service import AgentService
from src.utils.logger import get_logger

router = APIRouter()
service = AgentService()


logger = get_logger(__name__)


@router.get("/process/{num}")
async def process(num: int):
    logger.info(f"Received request to process method in router: {num}")
    return await service.invoke(num)
