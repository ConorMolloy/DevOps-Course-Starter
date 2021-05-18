from app.to_do_item import ToDoItem
from datetime import datetime

class TestToDoItem:
    def test_to_do_item_str(self):
        item = ToDoItem('123', 'Title', 'To Do', datetime(year=2021, month=5, day= 10, hour=10, minute=30, second=42, microsecond=123))

        assert str(item) == 'Title-To Do-2021-05-10 10:30:42.000123'

    def test_new_item_as_dict_returns_correct_object(self):
        dict_to_test = ToDoItem.new_item_as_dict("Testing static builder method")
        date_time_obj = datetime.strptime(dict_to_test["last_modified"], '%Y-%m-%d %H:%M:%S.%f')

        assert "Testing static builder method" == dict_to_test["title"]
        assert "To Do" == dict_to_test["status"]
        assert isinstance(date_time_obj, datetime)
