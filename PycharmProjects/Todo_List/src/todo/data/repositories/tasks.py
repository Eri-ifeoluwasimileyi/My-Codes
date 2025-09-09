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

    def _document_to_task(self, doc: dict) -> Task:
        return Task(id=str(doc["_id"]),
                title=doc.get("title"),
                description=doc.get("description"),
                priority=doc.get("priority"),
                status=doc.get("status"),
                flagged=doc.get("flagged", False),
                user_id=str(doc.get("user_id")) if doc.get("user_id") else None
            )

    def count_tasks(self) -> int:
        return self.collection.count_documents({})

    def save_task(self, task: Task):
        task_dict = task.model_dump()
        if self.exists_by_task_id(str(task.id)):
            self.collection.update_one({"_id": ObjectId(task.id)}, {"$set": task_dict})
        else:
            task_dict["_id"] = ObjectId(task.id) if task.id else ObjectId()
            self.collection.insert_one(task_dict)
            task.id = str(task_dict["_id"])
        return task

    def find_flagged(self) -> list[Task]:
        docs = self.collection.find({"flagged": True})
        return [self._document_to_task(doc) for doc in docs]

    def find_by_priority(self, priority: int) -> list[Task]:
        docs = self.collection.find({"priority": priority})
        return [self._document_to_task(doc) for doc in docs]

    def find_by_status(self, status: str) -> list[Task]:
        docs = self.collection.find({"status": status})
        return [self._document_to_task(doc) for doc in docs]

    def find_by_user_id(self, user_id: ObjectId) -> list[Task]:
        docs = self.collection.find({"user_id": user_id})
        return [self._document_to_task(doc) for doc in docs]

    def find_by_task_id(self, task_id: str) -> Optional[Task]:
        doc = self.collection.find_one({"_id": ObjectId(task_id)})
        return self._document_to_task(doc) if doc else None

    def delete_task_by_id(self, task_id: str) -> None:
        self.collection.delete_one({"_id": ObjectId(task_id)})

    def exists_by_task_id(self, task_id: str) -> bool:
        found_one = self.collection.find_one({"_id": ObjectId(task_id)})
        return found_one is not None

