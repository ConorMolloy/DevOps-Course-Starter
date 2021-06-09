"""The Enum that specifies the authorisation roles of the app"""
from enum import Enum

class Role(Enum):
    """The READER role is a read-only role, the WRITER can modify data"""
    READER = 'reader'
    WRITER = 'writer'
