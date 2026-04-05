from fastapi import FastAPI
from src.api.routes import router
import uvicorn
from src.utils.logger import setup_logger

setup_logger()

app = FastAPI(title="Fast API with processpool and Sigle Event Loop Feature Check")
app.include_router(router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
