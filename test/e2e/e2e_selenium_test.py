from datetime import time
import pytest
from app.create_app import create_app
from app.flask_config import Config
from app.atlas_client import AtlasClient
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

    app_config = Config()
    app_config._todo_collection_name = os.environ.get('TEST_COLLECTION')
    db_client = pymongo.MongoClient(f"{app_config.db_url}")
    db = db_client[f"{app_config.db_name}"]
    client = AtlasClient(db, app_config)

    application = create_app(client, app_config)

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
    driver.implicitly_wait(10)
    driver.get('http://localhost:5000/')
    driver.implicitly_wait(10)
    driver.find_element_by_id('item').send_keys(test_item_name)
    driver.implicitly_wait(10)
    driver.find_element_by_id('submit').click()
    driver.implicitly_wait(10)
    driver.find_element_by_id(test_item_name+'_complete').click()
    driver.implicitly_wait(10)
    driver.find_element_by_id(test_item_name+'_delete').click()

    assert test_item_name not in driver.page_source