class ToDoItem(object):
    def __init__(self, id, status, title):
        self.id = id
        self.status = status
        self.title = title

    def __str__(self):
        return self.title+'-'+self.status
        