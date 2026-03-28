"""
# Routers in FastAPI
 The APIRouter in FastAPI is a powerful tool used to organize path operations into separate, modular files, which makes the codebase cleaner and easier to manage, especially for larger applications. It functions like a "mini-FastAPI" app that can be included in the main application

Key Features and Benefits
-  Modularity : Break your API into logical sections (e.g., a router for users and another for items).
-  Organization : Group related routes, dependencies, and configurations together.
-  Prefixes and Tags : Add a common URL prefix (e.g., /users) and tags (for documentation) to all routes in a single router.
-  Dependencies : Apply common dependencies (like authentication requirements) to all path operations within the router.
-  Automatic Documentation : Routes defined in a router are automatically included in the OpenAPI documentation (Swagger UI/ReDoc).

"""

# Include the Router in the Main App (e.g., main.py)
from fastapi import FastAPI
from routers.items_router import items_router
from routers.user_router import user_router
import uvicorn

app = FastAPI()

# Include the items router
app.include_router(user_router)
app.include_router(items_router)


@app.get("/")
async def main_route():
    return {"message": "Hello from the main app"}


# To start server you use uvicorn.run method
# Here important "reload=True" is that, Now if we running server but if you change logic of the file,
# then without stop server you can see latest changes.

if __name__ == "__main__":
    uvicorn.run("05_py_fastapirouter:app", host="0.0.0.0", port=8000, reload=True)
