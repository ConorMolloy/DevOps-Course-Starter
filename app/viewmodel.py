"""ViewModel"""
from datetime import datetime, date
from typing import List
from app.to_do_item import ToDoItem

class ViewModel:
    """ViewModel that will populate HTML templates"""
    def __init__(self, items:List[ToDoItem]):
        self._items = items

    @property
    def items(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return sorted(self._items, key=lambda item: item.status, reverse=True)

    @property
    def to_do(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return [item for item in self._items if item.status == "To Do"]

    @property
    def doing(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return [item for item in self._items if item.status == "Doing"]

    @property
    def done(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        return [item for item in self._items if item.status == "Done"]

    @property
    def show_all_done_items(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        if len(self.done) < 5:
            return self.done
        return self.recent_done_items

    @property
    def recent_done_items(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        today:date = datetime.now().date()

        done_items:List[ToDoItem] = self.done

        filtered_done_items = filter(lambda item: item.last_modified.date() == today , done_items)

        return list(filtered_done_items)

    @property
    def older_done_items(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        today:date = datetime.now().date()

        done_items:List[ToDoItem] = self.done

        filtered_done_items = filter(lambda item: item.last_modified.date() != today , done_items)

        return list(filtered_done_items)
