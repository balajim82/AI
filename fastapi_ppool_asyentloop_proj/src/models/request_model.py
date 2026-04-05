
from pydantic import BaseModel

class ProcessRequest(BaseModel):
    name: str
