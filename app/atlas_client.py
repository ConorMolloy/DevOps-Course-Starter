"""Client for Mongodb Atlas"""
from datetime import datetime
from typing import List
from bson.objectid import ObjectId
from pymongo.collection import ReturnDocument
from pymongo.database import Database
from app.to_do_item import ToDoItem
from app.flask_config import Config
from app.client_interface import ClientInterface

class AtlasClient(ClientInterface):
    """
    Args:
        ClientInterface: The interface that a client ned to conform to for the app to work
    """
    def __init__(self, db: Database, config: Config):
        self._db = db
        self._collection = db[config.todo_collection_name]

    def get_items(self) -> List[ToDoItem]:
        return list(map(lambda doc: ToDoItem.from_json(doc), self._collection.find())) # pylint:disable=unnecessary-lambda

    def get_item(self, item_id: str) -> ToDoItem:
        return ToDoItem.from_json(self._collection.find_one({"_id": ObjectId(item_id)}))

    def add_item(self, title: str) -> str:
        return str(self._collection.insert_one(ToDoItem.new_item_as_dict(title)).inserted_id)

    def mark_complete(self, item_id: str) -> ToDoItem:
        query: dict = { "_id": ObjectId(item_id)}
        new_status: dict = { "$set": {
            "status": "Done",
            "last_modified": str(datetime.now())
        }}
        return ToDoItem.from_json(
            self._collection.find_one_and_update(
                query, new_status, return_document=ReturnDocument.AFTER
                )
            )

    def delete_item_by_id(self, item_id: str) -> ToDoItem:
        return ToDoItem.from_json(self._collection.find_one_and_delete({"_id": ObjectId(item_id)}))
