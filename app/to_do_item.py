"""ToDoItem model class"""
from datetime import datetime
from typing import Type, TypeVar

T = TypeVar('T', bound='ToDoItem') # pylint:disable=invalid-name

class ToDoItem:
    """DTO for ToDoItems between the UI and the database
    """
    def __init__(self, item_id: str, title: str, status: str, last_modified: str):
        self._id = item_id
        self._status = status
        self._title = title
        self._last_modified = datetime.strptime(last_modified, '%Y-%m-%d %H:%M:%S.%f')

    @property
    def item_id(self) -> str:
        """
        Returns:
            str: the ToDoItem id
        """
        return self._id

    @property
    def title(self) -> str:
        """
        Returns:
            str: the ToDoItem title
        """
        return self._title

    @property
    def status(self) -> str:
        """
        Returns:
            str: the ToDoItem status (To Do|Done)
        """
        return self._status

    @property
    def last_modified(self) -> str:
        """
        Returns:
            str: the time the ToDoItem was last interacted with
        """
        return self._last_modified

    def __str__(self):
        return self.title+'-'+self.status+'-'+str(self.last_modified)

    @staticmethod
    def new_item_as_dict(title: str) -> dict:
        """This a static factory method that is used when the ObjectId of the database is not known
        ie. before it gets saved. It takes a title and auto-populates all of the other fields needed
        for the app to function

        Args:
            title (str): the title of the item

        Returns:
            dict: a dict representation of a ToDoItem that can be saved as a document in the db
        """
        return {
            "title": title,
            "status": "To Do",
            "last_modified": str(datetime.now())
        }

    @classmethod
    def from_json(cls: Type[T], incoming_object: object) -> T:
        """This is a static method for deserialising a ToDoItem from JSON to an eaily interacted
        with python object.

        Args:
            cls (Type[T]): The class type that is being used, in this case a ToDoItem
            incoming_object (object): the JSON (BSON) oject returned from a database

        Returns:
            T: ToDoItem
        """
        return cls(
            str(incoming_object["_id"]),
            incoming_object["title"],
            incoming_object["status"],
            incoming_object["last_modified"]
            )
