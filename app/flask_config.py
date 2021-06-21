"""Flask configuration classes"""
import os


class FlaskConfig:
    """Environment variables needed by Flask"""
    def __init__(self):
        self.SECRET_KEY = os.environ.get('SECRET_KEY') # pylint:disable=invalid-name
        self.OAUTHLIB_INSECURE_TRANSPORT = os.environ.get('OAUTHLIB_INSECURE_TRANSPORT') # pylint:disable=invalid-name

    @property
    def secret_key(self) -> str:
        """
        Returns:
            str: returns secret key for the app
        """
        return self.SECRET_KEY

    @property
    def oauthlib_insecure_transport(self) -> str:
        """
        Returns:
            str: returns oauthlib_insecure_transport
        """
        return self.OAUTHLIB_INSECURE_TRANSPORT

class AuthConfig:
    """Configuration for the apps authentication"""
    def __init__(self):
        self._client_id = os.environ.get('CLIENT_ID')
        self._client_secret = os.environ.get('CLIENT_SECRET')
        self._writer_user = os.environ.get('WRITER_USER')

    @property
    def client_id(self) -> str:
        """
        Returns:
            str: GitHub client id used for OAuth
        """
        return self._client_id

    @property
    def client_secret(self) -> str:
        """
        Returns:
            str: GitHub client secret used in the OAuth flow
        """
        return self._client_secret

    @property
    def writer_user(self) -> str:
        """
        Returns:
            str: The hardcoded user that has admin access
        """
        return self._writer_user


class DatabaseConfig:
    """Config class containing the environment variables needed for the app"""
    def __init__(self):
        self._db_url = os.environ.get('DB_URL')
        self._db_name = os.environ.get('DB_NAME')
        self._todo_collection_name = os.environ.get('TODO_COLLECTION_NAME')
        self._user_collection = os.environ.get('USER_COLLECTION_NAME')

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
    def user_collection(self) -> str:
        """
        Returns:
            str: name of the user colection
        """
        return self._user_collection

    @property
    def db_name(self) -> str:
        """
        Returns:
            str: database name used inside the Mongo cluster
        """
        return self._db_name
