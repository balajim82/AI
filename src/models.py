from typing import List, Union
from pydantic import BaseModel


class Condition(BaseModel):
    field: str
    op: str
    value: Union[int, float, str]


class AndCondition(BaseModel):
    AND: List["Query"]


class OrCondition(BaseModel):
    OR: List["Query"]


Query = Union[Condition, AndCondition, OrCondition]


AndCondition.model_rebuild()
OrCondition.model_rebuild()
