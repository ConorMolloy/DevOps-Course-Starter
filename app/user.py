"""User class for app auth"""
from flask_login import UserMixin
from app.role import Role

class User(UserMixin):
    """
    Args:
        UserMixin: This provides default implementations for the methods that Flask-Login
        expects user objects to have.
    """
    def __init__(self, user_id: str, role: str=Role.READER.value):
        self.id = user_id # pylint:disable=invalid-name
        self.role = role
