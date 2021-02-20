"""Flask configuration class."""
import os


class Config:
    def __init__(self):
        self._board_id = os.environ.get('BOARD_ID')
        self._key = os.environ.get('KEY')
        self._token = os.environ.get('TOKEN')

    @property
    def board_id(self) -> str:
        return self._board_id

    @property
    def key(self) -> str:
        return self._key

    @property
    def token(self) -> str:
        return self._token
