class ToDoItem(object):
    def __init__(self, id, status, title, last_modified):
        self.id = id
        self.status = status
        self.title = title
        self.last_modified = last_modified

    def __str__(self):
        return self.title+'-'+self.status+'-'+self.last_modified
        