from abc import ABC, abstractmethod
from typing import Optional

from bson import ObjectId

from  todo.data.models.task import Task


class TasksInterface(ABC):

    @abstractmethod
    def count_tasks(self) -> int:
        pass

    @abstractmethod
    def save_task(self, task: Task):
        pass

    @abstractmethod
    def find_by_task_id(self, task_id: str) -> Optional[Task]:
        pass

    @abstractmethod
    def find_by_user_id(self, user_id: ObjectId) -> list[Task]:
        pass

    @abstractmethod
    def find_by_status(self, status: str) -> list[Task]:
        pass

    @abstractmethod
    def find_by_priority(self, priority: int) -> list[Task]:
        pass

    @abstractmethod
    def find_flagged(self) -> list[Task]:
        pass

    @abstractmethod
    def delete_task_by_id(self, task_id: str) -> None:
        pass

    @abstractmethod
    def exists_by_task_id(self, task_id: str) -> bool:
        pass
