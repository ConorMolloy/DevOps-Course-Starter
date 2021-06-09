import pytest
from flask_login import LoginManager
from requests.models import Response
from app.create_app import create_app
from app.to_do_item import ToDoItem
from app.atlas_client import AtlasClient
from dotenv import find_dotenv, load_dotenv
from unittest.mock import Mock, patch
from app.flask_config import Config
import mongomock

def test_index_page():
    file_path = find_dotenv('.env.test', usecwd=True)
    load_dotenv(file_path, override=True)

    app_config = Config()

    mocked_db = mongomock.MongoClient().get_database("db")
    client = AtlasClient(mocked_db, app_config)
    login_manager = LoginManager()

    #Create the new app.
    test_app = create_app(client, app_config, login_manager)
    test_app.config['LOGIN_DISABLED'] = True

    mock_item_response = ToDoItem.new_item_as_dict("Hello form the integration tests")
    
    mocked_db.get_collection("test_collection_name").insert_one(mock_item_response)

    response = test_app.test_client().get("/")
    assert 200 == response.status_code
    assert "Hello form the integration tests" in response.data.decode()
    