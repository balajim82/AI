"""
Here discussing about Response Model.


"""

from fastapi import FastAPI, Path, Query, Body, HTTPException, status, Response
from typing import Optional, List
import uvicorn
from pydantic import BaseModel, Field, field_validator
from models.user_profile import UserProfile
from models.user_create import UserCreate
from models.user_response import UserResponse
from fastapi.responses import (
    JSONResponse,
    HTMLResponse,
    FileResponse,
    StreamingResponse,
)

app = FastAPI(
    title="My API", description="API for production services", version="1.0.0"
)
# Response Models


# Standard response model
@app.get("/users/{user_id}", response_model=UserResponse)
async def get_user(user_id: int):
    return {"id": user_id, "username": "john"}


# Exclude fields from response
@app.get(
    "/users/{user_id}/public",
    response_model=UserResponse,
    response_model_exclude={"email"},
)
async def get_user_public(user_id: int):
    return {"id": user_id, "username": "john", "email": "john@example.com"}


# Include only specific fields
@app.get(
    "/users/{user_id}/minimal",
    response_model=UserResponse,
    response_model_include={"id", "username"},
)
async def get_user_minimal(user_id: int):
    return {"id": user_id, "username": "john"}


# Custom status code
@app.post("/users/", status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate):
    return {"id": 1, "username": user.username}


# Return different response types
@app.get("/data/{format}")
async def get_data(format: str):
    data = {"key": "value"}

    if format == "json":
        return JSONResponse(content=data)
    elif format == "html":
        html_content = "<html><body><h1>Data</h1></body></html>"
        return HTMLResponse(content=html_content)
    else:
        return data


# Streaming response
import io


@app.get("/stream/")
async def stream_data():
    def generate():
        for i in range(100):
            yield f"data: {i}\n\n"

    return StreamingResponse(generate(), media_type="text/event-stream")


# File download
@app.get("/download/{filename}")
async def download_file(filename: str):
    file_path = f"/path/to/{filename}"
    return FileResponse(
        path=file_path, filename=filename, media_type="application/octet-stream"
    )


# Custom headers
@app.get("/custom-headers/")
async def custom_headers(response: Response):
    response.headers["X-Custom-Header"] = "Custom Value"
    response.set_cookie(key="session_id", value="abc123")
    return {"message": "Check headers"}


# To start server you use uvicorn.run method
# Here important "reload=True" is that, Now if we running server but if you change logic of the file,
# then without stop server you can see latest changes.

if __name__ == "__main__":
    uvicorn.run("04_py_fastapi_response:app", host="0.0.0.0", port=8000, reload=True)
