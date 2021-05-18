import pytest
import pymongo
from dotenv import find_dotenv, load_dotenv
from app.flask_config import Config
from app.atlas_client import AtlasClient
from app.to_do_item import ToDoItem
from datetime import datetime
from bson.objectid import ObjectId
import os

@pytest.fixture
def atlas_client() -> AtlasClient:
    file_path = find_dotenv('.env')
    load_dotenv(file_path, override=True)

    app_config = Config()
    app_config._todo_collection_name = os.environ.get('TEST_COLLECTION')
    db_client = pymongo.MongoClient(f"{app_config.db_url}")
    db = db_client[f"{app_config.db_name}"]
    
    return AtlasClient(db, app_config)

def test_get_items_returns_list_of_all_items_in_collection(atlas_client):
    items = [ToDoItem.new_item_as_dict("First Post"), ToDoItem.new_item_as_dict("Second Post")]
    
    atlas_client._collection.insert_many(items)

    response = atlas_client.get_items()
    atlas_client._collection.delete_many({})

    assert len(response) == 2
    for obj in response:
        assert isinstance(obj, ToDoItem)

def test_get_items_returns_empty_list_if_no_items_in_collection(atlas_client):
    response = atlas_client.get_items()

    assert len(response) == 0

def test_add_item_should_save_new_item_to_db_and_return_id(atlas_client):
    id = atlas_client.add_item("New Test TODO")
    returned_item = atlas_client._collection.find_one(ObjectId(id))
    atlas_client._collection.delete_one({"_id": ObjectId(id)})
    date_time_obj = datetime.strptime(returned_item["last_modified"], '%Y-%m-%d %H:%M:%S.%f')
    
    assert returned_item["title"] == "New Test TODO"
    assert returned_item["status"] == "To Do"
    assert isinstance(date_time_obj, datetime)

def test_get_item_should_return_correct_item_given_many_in_collection(atlas_client):
    items = [ToDoItem.new_item_as_dict("First Post"), ToDoItem.new_item_as_dict("Second Post")]
    atlas_client._collection.insert_many(items)

    string_id = atlas_client.add_item("The one I want")

    response_I_want = atlas_client.get_item(string_id)
    atlas_client._collection.delete_many({})
    
    assert "The one I want" == response_I_want.title

def test_mark_completed_updates_status_and_returns_updated_state(atlas_client):
    string_id = atlas_client.add_item("The one I want to update")

    updated_item = atlas_client.mark_complete(string_id)
    atlas_client._collection.delete_many({})

    assert "Done" == updated_item.status

def test_delete_item_by_id_deletes_item_and_returns_deleted_item(atlas_client):
    string_id = atlas_client.add_item("The one I want to delete")

    deleted_item = atlas_client.delete_item_by_id(string_id)

    items_in_collection = atlas_client.get_items()

    assert "The one I want to delete" == deleted_item.title
    assert len(items_in_collection) == 0