"""Flask configuration class."""
import os


class Config:
    """Base configuration variables."""
    SECRET_KEY = os.environ.get('SECRET_KEY')
    boardId = os.environ.get('boardId')
    key = os.environ.get('key')
    token = os.environ.get('token')
    if not SECRET_KEY:
        raise ValueError("No SECRET_KEY set for Flask application. Did you forget to run setup.sh?")
