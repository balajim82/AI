from fastapi import FastAPI
from src.service import QueryService
from src.models import Query
import uvicorn
from pydantic import BaseModel

app = FastAPI()
service = QueryService()


class QueryInput(BaseModel):
    query_input: str


@app.post("/parse_lark", response_model=Query)
def parse_query(data: QueryInput):
    return service.parse(data.query_input)


# To start server you use uvicorn.run method
# Here important "reload=True" is that, Now if we running server but if you change logic of the file,
# then without stop server you can see latest changes.

if __name__ == "__main__":
    # parse_query('price > 100 AND name = "Laptop" OR rating >= 4.5')
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
