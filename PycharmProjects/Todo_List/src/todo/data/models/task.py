from datetime import datetime, date, time
from enum import Enum
from typing import Optional

from bson import ObjectId

from pydantic import BaseModel, ConfigDict, Field


class Status(Enum):
    ACTIVE = 'active'
    COMPLETED = 'completed'


class Priority(Enum):
    LOW = 'low'
    MEDIUM = 'medium'
    HIGH = 'high'


class Task(BaseModel):
    title: str
    id: Optional[ObjectId] = Field(None, alias='_id')
    description: Optional[str] = None
    status: Status = Status.ACTIVE
    priority: Priority = Priority.LOW
    flagged: bool = False
    due_date: Optional[date] = None
    due_time: Optional[time] = None
    created_at: datetime = Field(default_factory=datetime.now, frozen=True)
    updated_at: Optional[datetime] = None
    completed_at: datetime = None
    user_id: ObjectId

    model_config = ConfigDict(from_attributes=True,
                              use_enum_values=True,
                              populate_by_name=True)