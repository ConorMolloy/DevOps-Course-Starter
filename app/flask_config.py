"""Flask configuration class."""
import os


class Config:
    def __init__(self):
        self._db_url = os.environ.get('DB_URL')
        self._db_name = os.environ.get('DB_NAME')
        self._todo_collection_name = os.environ.get('TODO_COLLECTION_NAME')

    @property
    def db_url(self) -> str:
        return self._db_url

    @property 
    def todo_collection_name(self) -> str:
        return self._todo_collection_name

    @property
    def db_name(self) -> str:
        return self._db_name