"""The Enum that specifies the authorisation roles of the app"""
from enum import Enum

class Role(Enum):
    """READER - read-only, WRITER - can modify data"""
    READER = 'reader'
    WRITER = 'writer'
