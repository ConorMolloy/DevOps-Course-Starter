"""Helper method that specifies the @autherize decorator"""
from functools import wraps
from flask import current_app, abort
from flask_login import current_user

def authorized_for(role: str):
    """Allows writer role to add items and throw a 401 when a reader tries
    to modify the data in the app
    Args:
        role (str): One of the options in the Role class
    """
    def autherize(func):
        @wraps(func)
        def decorated_view(*args, **kwargs):
            if current_user.role == role:
                return func(*args, **kwargs)
            return abort(401)
        return decorated_view
    return autherize
