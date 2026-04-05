import logging
from logging.handlers import RotatingFileHandler
import os


def setup_logger():
    os.makedirs("logs", exist_ok=True)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | PID:%(process)d | %(name)s | %(message)s"
    )

    file_handler = RotatingFileHandler(
        "logs/fastapi.log", maxBytes=5 * 1024 * 1024, backupCount=5
    )
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)


def get_logger(name: str):
    return logging.getLogger(name)
