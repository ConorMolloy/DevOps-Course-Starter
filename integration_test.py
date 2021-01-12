import json
from unittest import mock
import pytest
from requests.models import Response
import app
import requests
from dotenv import find_dotenv, load_dotenv
from unittest.mock import Mock, patch

@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version 
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)

    #Create the new app.
    test_app = app.create_app()
    
    # Use the app to create a test_client that can be used in our tests.
    with test_app.test_client() as client: 
        yield client

@patch('requests.get')
def test_index_page(mock_get_requests, client):
    mock_response = Response()
    mock_response.status_code = 200
    mock_response._content = b'{"id": "123", "idList": "987", "name": "Why hello there", "dateLastActivity": "2021-01-06T21:14:06.518Z"}'

    mock_get_requests.return_value = mock_response
    response = client.get('/')
    