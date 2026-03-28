"""
Fast api documentation - https://fastapi.tiangolo.com/tutorial/first-steps/
FastAPI is a modern, high-performance web framework for building APIs with Python 3.8+.
 1> This fastAPI is smiliar to RestAPI  in Java.
 2> In python we have alternative Flask also. but most widely used FastAPI.
 3> Flask follows MVC Structure so ui, backend both supports.
 4> But FastApi very good and provides good Performance and  suppots only backend. Develoed in "Go" Language.
 5> Fast API  supports and good  Understaing with Pydantic and asyncIO. So it followes and good understaning on these lib.
 6> I java when ever we run any web application we need server like Tomcat/weblogc/Jboss.
    Here to run any api/web application we need one server that's called "uvicorn".
    This server can hanldle mulitpleworkers as well.
  7> To show which version "uvicorn" installed.
      pip show uvicorn
  8> Using fastapi, can check path, query, body params how will pass it from api.
  9>


Key features:
 1. Fast: Performance comparable to NodeJS and Go (thanks to Starlette and Pydantic)
 2. Type hints: Leverages Python type hints for validation and documentation
 3. Auto-docs: Automatic interactive API documentation (Swagger UI & ReDoc)
 4. Standards-based: Built on OpenAPI and JSON Schema
 5. Async support: Native async/await support for high concurrency
 6. Dependency injection: Powerful DI system for clean architecture

"""

# Basic Sample Program
from fastapi import FastAPI, Path, Query, Body
from typing import Optional, List
import uvicorn
from pydantic import BaseModel

app = FastAPI(
    title="My API", description="API for production services", version="1.0.0"
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/health")
async def health_check():
    return {"status": "healthy"}


# This Path Single Params meter.
@app.get("/users/{user_id}")
async def getuser(user_id: int):
    return {"user_id": user_id}


# This Path mullti Params meter.
@app.get("/orders/{order_name}/users/{user_id}")
async def getuser(order_name: str, user_id: int):
    return {"order_name": order_name, "user_id": user_id}


# Query parameters
""" When you declare other function parameters that are not part of the path parameters,
they are automatically interpreted as "query" parameters. """


@app.get("/items_part/")
async def list_items_part(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, le=100),
    search: Optional[str] = None,
):
    return {"skip": skip, "limit": limit, "search": search}


# Request Handling - Different Request Types
from fastapi import FastAPI, Form, File, UploadFile, Header, Cookie
from typing import List, Optional

app = FastAPI()


# Form data
@app.post("/login/")
async def login(username: str = Form(...), password: str = Form(...)):
    return {"username": username}


# File upload
@app.post("/upload/")
async def upload_file(file: UploadFile = File(...)):
    contents = await file.read()
    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "size": len(contents),
    }


# Multiple files
@app.post("/uploadfiles/")
async def upload_files(files: List[UploadFile] = File(...)):
    return [{"filename": f.filename} for f in files]


# Headers
@app.get("/items/")
async def read_items(
    user_agent: Optional[str] = Header(None),
    accept_language: Optional[str] = Header(None),
):
    return {"User-Agent": user_agent, "Accept-Language": accept_language}


# Cookies
@app.get("/analytics/")
async def get_analytics(
    session_id: Optional[str] = Cookie(None), user_id: Optional[str] = Cookie(None)
):
    return {"session_id": session_id, "user_id": user_id}


# Complex request body
class SearchQuery(BaseModel):
    query: str
    filters: dict = {}
    sort_by: Optional[str] = None
    page: int = 1
    page_size: int = 10


@app.post("/search/")
async def search(query: SearchQuery):
    return {"query": query.query, "total_results": 100, "results": []}


# To start server you use uvicorn.run method
# Here important "reload=True" is that, Now if we running server but if you change logic of the file,
# then without stop server you can see latest changes.

if __name__ == "__main__":
    uvicorn.run("02_py_fastapi:app", host="0.0.0.0", port=8000, reload=True)
