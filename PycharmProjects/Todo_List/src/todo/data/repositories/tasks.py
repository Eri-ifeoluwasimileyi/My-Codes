from typing import Optional

from bson import ObjectId
from fastapi import Depends
from pymongo.synchronous.database import Database

from todo.configurations.database_configuration import get_db_connection
from todo.data.models.task import Task
from todo.data.repositories.tasks_interface import TasksInterface


class TaskRepository(TasksInterface):
    def __init__(self, db: Database = Depends(get_db_connection)):
        self.db = db
        self.collection = self.db["tasks"]

    def count_tasks(self) -> int:
       return self.collection.count_documents({})

    def save_task(self, task: Task):
        if self.exists_by_task_id(str(task.id)):
            pass

    def find_flagged(self) -> list[Task]:
        pass

    def find_by_priority(self, priority: int) -> list[Task]:
        pass

    def find_by_status(self, status: str) -> list[Task]:
        pass

    def find_by_user_id(self, user_id: ObjectId) -> list[Task]:
        pass

    def find_by_task_id(self, task_id: str) -> Optional[Task]:
        pass

    def delete_task_by_id(self, task_id: str) -> None:
        pass

    def exists_by_task_id(self, task_id: str) -> bool:

        found_one = self.collection.find_one({"_id": ObjectId(task_id)})
        return found_one is not None