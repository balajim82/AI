"""
# Dependency Management
In FastAPI,  Depends  is the core mechanism for dependency injection, a powerful pattern for declaring the shared logic or resources a function needs to run. FastAPI automatically handles providing these dependencies, making code modular, reusable, and easy to test.
 How Depends Works
1.  Define a "Dependable" : You create a Python function or class (a "callable") that performs a specific task, such as fetching data, validating a token, or creating a database session. This function can take parameters itself, which FastAPI resolves from the request (e.g., query parameters, headers).
2.  Declare the Dependency : In a path operation function (an endpoint), you use Depends() within the function's parameters to tell FastAPI that this function relies on the "dependable".
3.  FastAPI Handles the Injection : When a request arrives, FastAPI takes over:

- It calls the dependency function with the required parameters extracted from the request.
- It gets the return value from the dependency.
- It "injects" that return value into the path operation function's corresponding parameter.
- If a dependency raises an HTTPException, the path operation function won't run, and the error will be returned to the client.

 Key Concepts & Use Cases
-  Code Reusability:  Avoid repeating the same logic (like authentication or pagination parameters) in multiple endpoints by defining it once as a dependency.
-  Authentication & Security : A common use is to enforce security by creating a dependency that validates an API key or a JWT token and returns the current user.
-  Database Connections : Dependencies can manage the lifecycle of resources, such as creating a database session when a request starts and ensuring it's closed (using yield) after the response is sent.
-  Testing : This system simplifies testing. You can easily replace real dependencies with mock or fake versions using FastAPI's dependency_overrides feature during tests.
-  Sub-dependencies : Dependencies can depend on other dependencies, creating a nested "tree" of logic that FastAPI resolves automatically and in the correct order.

"""

# Basic Dependencies

from fastapi import FastAPI, Depends, HTTPException, Header, BackgroundTasks
from typing import Optional
import uvicorn
import time
from models.user_create import UserCreate


app = FastAPI()


# Simple dependency
async def get_query_param(q: Optional[str] = None):
    return q


@app.get("/items/")
async def read_items(query: Optional[str] = Depends(get_query_param)):
    return {"query": query}


# Dependency with validation
async def pagination_params(skip: int = 0, limit: int = 10):
    if limit > 100:
        raise HTTPException(status_code=400, detail="Limit too high")
    return {"skip": skip, "limit": limit}


@app.get("/users/")
async def list_users(pagination: dict = Depends(pagination_params)):
    return {"skip": pagination["skip"], "limit": pagination["limit"], "users": []}


# Class-based dependency
class CommonQueryParams:
    def __init__(self, q: Optional[str] = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit


@app.get("/items/")
async def read_items(commons: CommonQueryParams = Depends()):
    return {"q": commons.q, "skip": commons.skip, "limit": commons.limit}


# Background Tasks


def send_email(email: str, message: str):
    """Simulate sending email"""
    time.sleep(2)  # Simulate email sending delay
    print(f"Email sent to {email}: {message}")


def log_activity(user_id: int, action: str):
    """Log user activity"""
    print(f"User {user_id} performed: {action}")


# To start server you use uvicorn.run method
# Here important "reload=True" is that, Now if we running server but if you change logic of the file,
# then without stop server you can see latest changes.

if __name__ == "__main__":
    uvicorn.run("06_py_fastapi_dependency:app", host="0.0.0.0", port=8000, reload=True)
