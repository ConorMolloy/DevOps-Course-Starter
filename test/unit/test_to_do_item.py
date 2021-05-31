from app.to_do_item import ToDoItem
from datetime import datetime
from mongomock import MongoClient

class TestToDoItem:
    def test_to_do_item_str(self):
        item = ToDoItem('123', 'Title', 'To Do', '2021-05-10 10:30:42.000123')

        assert str(item) == 'Title-To Do-2021-05-10 10:30:42.000123'

    def test_new_item_as_dict_returns_correct_object(self):
        dict_to_test = ToDoItem.new_item_as_dict("Testing static builder method")
        date_time_obj = datetime.strptime(dict_to_test["last_modified"], '%Y-%m-%d %H:%M:%S.%f')

        assert "Testing static builder method" == dict_to_test["title"]
        assert "To Do" == dict_to_test["status"]
        assert isinstance(date_time_obj, datetime)

    def test_get_from_json(self):
        test_object: dict = ToDoItem.new_item_as_dict("Testing static constructor method")

        collection = MongoClient().db.collection
        collection.insert_one(test_object)
        returned_object = collection.find_one({'title': 'Testing static constructor method'})

        object_to_test: ToDoItem = ToDoItem.from_json(returned_object)

        assert isinstance(object_to_test.item_id, str)
        assert "Testing static constructor method" == object_to_test.title
        assert "To Do" == object_to_test.status
        assert isinstance(object_to_test.last_modified, datetime)