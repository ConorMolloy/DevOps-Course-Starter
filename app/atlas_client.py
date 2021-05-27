from app.to_do_item import ToDoItem
from app.flask_config import Config
from app.client_interface import ClientInterface
from bson.objectid import ObjectId 
from datetime import datetime
from pymongo.collection import ReturnDocument
from pymongo.database import Database
from typing import List

class AtlasClient(ClientInterface):
    def __init__(self, db: Database, config: Config):
        self._db = db
        self._collection = db[config.todo_collection_name]

    def get_items(self) -> List[ToDoItem]:
        return list(map(lambda doc: ToDoItem.from_json(doc), list(self._collection.find())))

    def get_item(self, id: str) -> ToDoItem:
        return ToDoItem.from_json(self._collection.find_one({"_id": ObjectId(id)}))

    def add_item(self, title: str) -> str:
        return str(self._collection.insert_one(ToDoItem.new_item_as_dict(title)).inserted_id)

    def mark_complete(self, id: str) -> ToDoItem:
        query: dict = { "_id": ObjectId(id)}
        new_status: dict = { "$set": { 
            "status": "Done",
            "last_modified": str(datetime.now())
        }} 
        return ToDoItem.from_json(self._collection.find_one_and_update(query, new_status, return_document=ReturnDocument.AFTER))

    def delete_item_by_id(self, id: str) -> ToDoItem:
        return ToDoItem.from_json(self._collection.find_one_and_delete({"_id": ObjectId(id)}))
