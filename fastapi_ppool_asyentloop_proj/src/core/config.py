from pydantic_settings import BaseSettings
from src.utils.logger import get_logger

logger = get_logger(__name__)


class Settings(BaseSettings):
    logger.info(f"Start loading configuration settings")
    APP_NAME: str = "Clean FastAPI App"
    WORKER_MODE: str = "process"  # "async"  # or "process"
    logger.info(f"End loading configuration settings")


settings = Settings()
