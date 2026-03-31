import uvicorn
from fastapi import FastAPI
from src.controllers.inv_mgmt_cud_router import imcud_router
from src.controllers.inv_mgmt_read_reports import imrr_router

# To start server you use uvicorn.run method
# Here important "reload=True" is that, Now if we running server but if you change logic of the file,
# then without stop server you can see latest changes.
productapp = FastAPI(
    title="This is Inventory Management API ",
    description="API for production services",
    version="1.0.0",
)
# Include the Inv mgmt router
productapp.include_router(imcud_router, prefix="/api")
productapp.include_router(imrr_router, prefix="/api")


@productapp.get("/")
async def root():
    return {"message": "Inventory Management API Running.."}


if __name__ == "__main__":
    uvicorn.run("main:productapp", host="0.0.0.0", port=8000, reload=True)
