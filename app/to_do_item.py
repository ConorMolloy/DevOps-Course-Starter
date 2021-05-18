from datetime import datetime

class ToDoItem(object):
    def __init__(self, id: str, title: str, status: str, last_modified: datetime):
        self._id = id
        self._status = status
        self._title = title
        self._last_modified = last_modified

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
        