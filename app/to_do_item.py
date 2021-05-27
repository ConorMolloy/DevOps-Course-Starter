from datetime import datetime
from typing import Type, TypeVar

T = TypeVar('T', bound='ToDoItem')

class ToDoItem(object):
    def __init__(self, id: str, title: str, status: str, last_modified: str):
        self._id = id
        self._status = status
        self._title = title
        self._last_modified = datetime.strptime(last_modified, '%Y-%m-%d %H:%M:%S.%f')

    @property
    def id(self) -> str:
        return self._id

    @property
    def title(self) -> str:
        return self._title

    @property
    def status(self) -> str:
        return self._status

    @property
    def last_modified(self) -> str:
        return self._last_modified

    def __str__(self):
        return self.title+'-'+self.status+'-'+str(self.last_modified)

    @staticmethod
    def new_item_as_dict(title: str) -> dict: 
        return {
            "title": title,
            "status": "To Do",
            "last_modified": str(datetime.now())
        }

    @classmethod
    def from_json(cls: Type[T], incoming_object: object) -> T:
        return cls(str(incoming_object["_id"]), incoming_object["title"], incoming_object["status"], incoming_object["last_modified"])