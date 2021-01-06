class ViewModel:
    def __init__(self, items):
        self._items = items

    @property
    def items(self):
        return self._items

    @property
    def to_do(self):
        return [item for item in self._items if item.status == "To Do"]

    @property
    def doing(self):
        return [item for item in self._items if item.status == "Doing"]

    @property
    def done(self):
        return [item for item in self._items if item.status == "Done"]