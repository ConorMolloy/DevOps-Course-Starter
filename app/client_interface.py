"""ClientInterface"""
from abc import ABC, abstractmethod
from typing import List
from app.to_do_item import ToDoItem

class ClientInterface(ABC):
    """Interface that clients must conform to for the app to finction"""
    @abstractmethod
    def get_items(self) -> List[ToDoItem]:
        """
        Returns:
            List[ToDoItem]
        """

    @abstractmethod
    def get_item(self, item_id: str) -> ToDoItem:
        """
        Args:
            item_id (str): str version of the item id

        Returns:
            ToDoItem
        """

    @abstractmethod
    def add_item(self, title: str) -> str:
        """
        Args:
            title (str): title of the item you are adding to the list

        Returns:
            str: str id of the added item
        """

    @abstractmethod
    def mark_complete(self, item_id: str) -> ToDoItem:
        """
        Args:
            item_id (str): str version of the item id

        Returns:
            ToDoItem: ToDoItem that has been marked as complete
        """

    @abstractmethod
    def delete_item_by_id(self, item_id: str) -> ToDoItem:
        """
        Args:
            item_id (str): str version of the item id

        Returns:
            ToDoItem: ToDoItem that has been deleted
        """
