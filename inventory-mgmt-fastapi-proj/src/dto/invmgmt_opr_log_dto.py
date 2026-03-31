from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class InvenotryMgmtOprLogDTO(BaseModel):
    imolid: Optional[int]
    imolaction: str
    imoltimestamp: datetime
