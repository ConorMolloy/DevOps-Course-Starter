import os
import pytest
import time
import app
from selenium import webdriver
from threading import Thread

@pytest.fixture(scope='module')
def test_app():
    # construct the new application
    application = app.create_app()

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
    driver.get('http://localhost:5000/')
    assert driver.title == 'To-Do App'