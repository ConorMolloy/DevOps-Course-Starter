from abc import ABC, abstractmethod
from typing import List
from app.to_do_item import ToDoItem

class ClientInterface(ABC):
    @abstractmethod
    def get_items(self) -> List[ToDoItem]:
        pass

    @abstractmethod
    def get_item(self, id: str) -> ToDoItem:
        pass

    @abstractmethod
    def add_item(self, title: str) -> str:
        pass

    @abstractmethod
    def mark_complete(self, id: str) -> ToDoItem:
        pass

    @abstractmethod
    def delete_item_by_id(self, id: str) -> ToDoItem:
        pass