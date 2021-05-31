"""Flask configuration class."""
import os


class Config:
    """Config class containing the environment variables needed for the app
    """
    def __init__(self):
        self._db_url = os.environ.get('DB_URL')
        self._db_name = os.environ.get('DB_NAME')
        self._todo_collection_name = os.environ.get('TODO_COLLECTION_NAME')

    @property
    def db_url(self) -> str:
        """
        Returns:
            str: database url needed to conect to Mongo
        """
        return self._db_url

    @property
    def todo_collection_name(self) -> str:
        """
        Returns:
            str: collection name that the todo items will be saved in
        """
        return self._todo_collection_name

    @property
    def db_name(self) -> str:
        """
        Returns:
            str: database name used inside the Mongo cluster
        """
        return self._db_name
