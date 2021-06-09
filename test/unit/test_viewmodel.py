from app.viewmodel import ViewModel
from app.to_do_item import ToDoItem
from app.user import User
from app.role import Role
from datetime import datetime, timedelta

class TestViewModel:

    test_user = User('MrTestUser', Role.WRITER.value)

    def test_items(self):
        first_item = ToDoItem("1234", "First Test Item", "To Do", '2021-01-06 21:14:06.518')
        second_item = ToDoItem("4321", "In progress Item", "Doing", '2021-01-06 21:14:06.518')

        item_list = [first_item, second_item]
        view_model_under_test = ViewModel(item_list, self.test_user)

        diff = set(item_list) ^ set(view_model_under_test.items)

        assert len(item_list) == len(view_model_under_test.items)
        
        assert not diff

    def test_to_do(self):
        first_item = ToDoItem("1234", "First Test Item", "To Do", '2021-01-06 21:14:06.518')
        second_item = ToDoItem("4321", "In progress Item", "Doing", '2021-01-06 21:14:06.518')
        third_item = ToDoItem("1111", "I hope this test passes", "Done", '2021-01-06 21:14:06.518')

        item_list = [first_item, second_item, third_item]

        view_model_under_test = ViewModel(item_list, self.test_user)

        assert view_model_under_test.to_do == [first_item]

    def test_doing(self):
        first_item = ToDoItem("1234", "First Test Item", "To Do", '2021-01-06 21:14:06.518')
        second_item = ToDoItem("4321", "In progress Item", "Doing", '2021-01-06 21:14:06.518')
        third_item = ToDoItem("1111", "I hope this test passes", "Done", '2021-01-06 21:14:06.518')

        item_list = [first_item, second_item, third_item]

        view_model_under_test = ViewModel(item_list, self.test_user)

        assert view_model_under_test.doing == [second_item]

    def test_done(self):
        first_item = ToDoItem("1234", "First Test Item", "To Do", '2021-01-06 21:14:06.518')
        second_item = ToDoItem("4321", "In progress Item", "Doing", '2021-01-06 21:14:06.518')
        third_item = ToDoItem("1111", "I hope this test passes", "Done", '2021-01-06 21:14:06.518')

        item_list = [first_item, second_item, third_item]

        view_model_under_test = ViewModel(item_list, self.test_user)

        assert view_model_under_test.done == [third_item]

    def test_show_all_done_items_more_than_five(self):
        today = datetime.now()
        yesterday = datetime.now() + timedelta(days=-1)

        one = ToDoItem("1", "One", "Done", str(today))
        two = ToDoItem("2", "One", "Done", str(today))
        three = ToDoItem("3", "One", "Done", str(yesterday))
        four = ToDoItem("4", "One", "Done", str(yesterday))
        five = ToDoItem("5", "One", "Done", str(yesterday))
        six = ToDoItem("6", "One", "Done", str(yesterday))

        item_list = [one, two, three, four, five, six]

        view_model_under_test = ViewModel(item_list, self.test_user)

        assert view_model_under_test.show_all_done_items == [one, two]

    def test_show_all_done_items_less_than_five(self):
        today = datetime.now()
        yesterday = datetime.now() + timedelta(days=-1)

        one = ToDoItem("1", "One", "Done", str(today))
        two = ToDoItem("2", "One", "Done", str(today))
        three = ToDoItem("3", "One", "Done", str(yesterday))
        four = ToDoItem("4", "One", "Done", str(yesterday))

        item_list = [one, two, three, four]

        view_model_under_test = ViewModel(item_list, self.test_user)

        assert view_model_under_test.show_all_done_items == [one, two, three, four]

    def test_recent_done_items(self):
        today = datetime.now()
        tomorrow = today + timedelta(days=1)
        yesterday = today + timedelta(days=-1)

        first_item = ToDoItem("1234", "First Test Item", "Done", str(yesterday))
        second_item = ToDoItem("4321", "In progress Item", "Done", str(today))
        third_item = ToDoItem("1111", "I hope this test passes", "Done", str(tomorrow))

        item_list = [first_item, second_item, third_item]

        view_model_under_test = ViewModel(item_list, self.test_user)
        assert view_model_under_test.recent_done_items == [second_item]

    def test_older_done_items(self):
        today = datetime.now()
        yesterday = today + timedelta(days=-1)

        first_item = ToDoItem("1234", "First Test Item", "Done", str(yesterday))
        second_item = ToDoItem("4321", "In progress Item", "Done", str(today))
        third_item = ToDoItem("1111", "I hope this test passes", "Done", str(yesterday))

        item_list = [first_item, second_item, third_item]

        view_model_under_test = ViewModel(item_list, self.test_user)
        assert view_model_under_test.older_done_items == [first_item, third_item]