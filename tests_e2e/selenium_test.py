from datetime import time
import pytest
import app
import time
from selenium import webdriver
from threading import Thread

@pytest.fixture(scope='module')
def test_app():
    # construct the new application
    application = app.create_app()
    time.sleep(1)

    # start the app in its own thread.
    thread = Thread(target=lambda: application.run(use_reloader=False)) 
    thread.daemon = True
    thread.start()
    yield application 

    # Tear Down
    thread.join(1) 
    
@pytest.fixture(scope="module")
def driver():
    with webdriver.Firefox() as driver:
        yield driver

def test_task_journey(driver, test_app): 
    test_item_name = 'Finish selenium test'
    driver.get('http://localhost:5000/')
    driver.find_element_by_id('item').send_keys(test_item_name)
    driver.find_element_by_id('submit').click()
    time.sleep(1)
    driver.find_element_by_id(test_item_name+'_complete').click()
    time.sleep(1)
    driver.find_element_by_id(test_item_name+'_delete').click()

    assert driver.title == 'To-Do App'