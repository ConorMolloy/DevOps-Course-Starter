from app.to_do_item import ToDoItem
from app.flask_config import Config
from bson.objectid import ObjectId 
from datetime import datetime
from pymongo.collection import ReturnDocument
from pymongo.database import Database
from typing import List

class AtlasClient:
    def __init__(self, db: Database, config: Config):
        self._db = db
        self._collection = db[f'{config.todo_collection_name}']

    def get_items(self) -> List[ToDoItem]:
        return list(map(lambda doc: ToDoItem(str(doc["_id"]), doc["title"], doc["status"], doc["last_modified"]), list(self._collection.find())))

    def get_item(self, id: str) -> ToDoItem:
        returned_item: ToDoItem = self._collection.find_one({"_id": ObjectId(id)})
        return ToDoItem(str(returned_item["_id"]), returned_item["title"], returned_item["status"], returned_item["last_modified"])

    def add_item(self, title: str) -> str:
        return str(self._collection.insert_one(ToDoItem.new_item_as_dict(title)).inserted_id)

    def mark_complete(self, id: str) -> ToDoItem:
        query: dict = { "_id": ObjectId(id)}
        new_status: dict = { "$set": { 
            "status": "Done",
            "last_modified": str(datetime.now())
        }}
        updated_item = self._collection.find_one_and_update(query, new_status, return_document=ReturnDocument.AFTER)
        return ToDoItem(str(updated_item["_id"]), updated_item["title"], updated_item["status"], updated_item["last_modified"])

    def delete_item_by_id(self, id: str) -> ToDoItem:
        deleted_item = self._collection.find_one_and_delete({"_id": ObjectId(id)})
        return ToDoItem(str(deleted_item["_id"]), deleted_item["title"], deleted_item["status"], deleted_item["last_modified"])
