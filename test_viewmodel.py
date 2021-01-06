from viewmodel import ViewModel
from to_do_item import ToDoItem

class TestViewModel:
    def test_items(self):
        first_item = ToDoItem("1234", "To Do", "First Test Item")
        second_item = ToDoItem("4321", "Doing", "In progress Item")

        item_list = [first_item, second_item]

        view_model_under_test = ViewModel(item_list)

        assert view_model_under_test.items == item_list

    def test_to_do(self):
        first_item = ToDoItem("1234", "To Do", "First Test Item")
        second_item = ToDoItem("4321", "Doing", "In progress Item")
        third_item = ToDoItem("1111", "Done", "I hope this test passes")

        item_list = [first_item, second_item, third_item]

        view_model_under_test = ViewModel(item_list)

        assert view_model_under_test.to_do == [first_item]

    def test_doing(self):
        first_item = ToDoItem("1234", "To Do", "First Test Item")
        second_item = ToDoItem("4321", "Doing", "In progress Item")
        third_item = ToDoItem("1111", "Done", "I hope this test passes")

        item_list = [first_item, second_item, third_item]

        view_model_under_test = ViewModel(item_list)

        assert view_model_under_test.doing == [second_item]

    def test_done(self):
        first_item = ToDoItem("1234", "To Do", "First Test Item")
        second_item = ToDoItem("4321", "Doing", "In progress Item")
        third_item = ToDoItem("1111", "Done", "I hope this test passes")

        item_list = [first_item, second_item, third_item]

        view_model_under_test = ViewModel(item_list)

        assert view_model_under_test.done == [third_item]