from datetime import datetime, date, time
from typing import Optional

from bson import ObjectId
from pydantic import BaseModel, Field, ConfigDict



class CreateTaskResponse(BaseModel):
    title: str
    id: [ObjectId] =  Field(alias="_id")
    description: Optional[str] = None
    priority: str = None
    flagged: bool = None
    due_date: Optional[date] = None
    due_time: Optional[time] = None

    model_config = ConfigDict(validate_assignment=True,
                              from_attributes=True, populate_by_name=True,
                              json_encoders={
                                ObjectId: str,
                                date: lambda d: d.strftime("%m/%d/%Y"),
                                time: lambda d: d.strftime("%H:%M:%S")
                              }
    )


class UpdateTaskResponse(BaseModel):
    title: str
    id: [ObjectId] =  Field(alias="_id")
    description: Optional[str] = None
    priority: str = None
    flagged: bool = None
    due_date: Optional[date] = None
    due_time: Optional[time] = None
    updated_at: Optional[datetime] = None


    model_config = ConfigDict(validate_assignment=True, from_attributes =True,
                    json_encoders = {ObjectId: str,
                        date: lambda d: d.strftime("%m/%d/%Y"),
                        time: lambda d: d.strftime("%H:%M:%S"),
                        datetime: lambda dt: dt.isoformat(sep=' ', timespec='seconds')
                     }
    )


class DeleteTaskResponse(BaseModel):
    message: str
    deleted_at: Optional[datetime] = None