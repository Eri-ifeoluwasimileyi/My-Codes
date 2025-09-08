from abc import ABC, abstractmethod

from pydantic import EmailStr

from todo.data.models.user import User


class UserInterface(ABC):

    @abstractmethod
    def count_users(self) -> int:
        pass

    @abstractmethod
    def save(self, user: User) -> User:
        pass

    @abstractmethod
    def find_user_by_email(self, email: str) -> User:
        pass

    @abstractmethod
    def find_user_by_id(self, user_id: str) -> User:
        pass

    @abstractmethod
    def delete_by_id(self, user_id: str) -> None:
        pass

    @abstractmethod
    def exists_by_id(self, user_id: str) -> bool:
        pass