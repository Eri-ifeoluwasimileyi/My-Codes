from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field, ConfigDict


class User(BaseModel):
    id: Optional[ObjectId] = Field(default=None, alias="id")
    first_name: str
    last_name: str
    email: str
    password: str
    tasks: list[ObjectId]


    model_config = ConfigDict(from_attributes=True, populate_by_name=True)