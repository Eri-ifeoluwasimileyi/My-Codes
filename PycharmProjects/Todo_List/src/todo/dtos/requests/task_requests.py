from datetime import time, datetime
from typing import Optional

from pydantic import BaseModel, Field, FutureDate, ConfigDict

from todo.data.models.task import Status, Priority


class CreateTaskRequest(BaseModel):
    title: str = Field(..., min_length=1)
    description: Optional[str] = Field(None, min_length=1)
    priority: Optional[Priority] = Priority.LOW
    flagged: bool = False
    due_date: Optional[FutureDate] = None
    due_time: Optional[time] = None

    model_config = ConfigDict(validate_assignment=True, from_attributes=True)

class UpdateTaskRequest(BaseModel):
    title: str = Field(None, min_length=1)
    description: Optional[str] = Field(default=None, min_length=1)
    priority: Optional[Priority] = None
    flagged: bool = None
    due_date: Optional[FutureDate] = None
    due_time: Optional[time] = None

    model_config = ConfigDict(validate_assignment=True, from_attributes=True)

class DeleteTaskRequest(BaseModel):
    task_id: str