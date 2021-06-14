from datetime import time
import pytest
from flask_login import LoginManager
from pymongo import MongoClient
from unittest.mock import patch
from app.create_app import create_app
from app.flask_config import DatabaseConfig, AuthConfig, FlaskConfig
from app.atlas_client import AtlasClient
from app.role import Role
from test.test_user import TestUser
import time
from selenium import webdriver
from threading import Thread
from dotenv import find_dotenv, load_dotenv
from selenium.webdriver.firefox.options import Options
import pymongo
import os

@pytest.fixture(scope='module')
def test_app():
    # construct the new application
    try:
        file_path = find_dotenv('.env')
        load_dotenv(file_path, override=True)
    except:
        print("Could not find .env")

    database_config = DatabaseConfig()
    auth_config = AuthConfig()
    flask_config = FlaskConfig()
    database_config._todo_collection_name = os.environ.get('TEST_COLLECTION')
    mongo_client = MongoClient(database_config.db_url)
    client = AtlasClient(database_config, mongo_client)
    client._collection.delete_many({})
    login_manager = LoginManager()
    login_manager.anonymous_user = TestUser

    application = create_app(client, auth_config, flask_config, login_manager)
    application.config['LOGIN_DISABLED'] = True

    # start the app in its own thread.
    thread = Thread(target=lambda: application.run(use_reloader=False)) 
    thread.daemon = True
    thread.start()
    yield application 

    # Tear Down
    thread.join(1) 
    
@pytest.fixture(scope="module")
def driver():
    options = Options()
    options.headless =  True
    with webdriver.Firefox(options=options) as driver:
        yield driver

def test_task_journey(driver, test_app):
    test_item_name = 'Finish selenium test'
    # this is to stop a connection issue that was causing intermittant failures
    time.sleep(3)
    driver.get('http://localhost:5000/')
    assert 'To-Do App' in driver.title
    driver.find_element_by_id('item').send_keys(test_item_name)
    driver.find_element_by_id('submit').click()
    driver.find_element_by_id(test_item_name+'_complete').click()
    driver.find_element_by_id(test_item_name+'_delete').click()

    assert test_item_name not in driver.page_source