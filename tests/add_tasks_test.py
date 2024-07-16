import unittest
import functions


class TestAddTask(unittest.TestCase):

    def test_add_task_positive(self):
        functions.tasks_list = []
        with unittest.mock.patch('builtins.input', return_value='Test Task'):
            functions.add_task(functions.tasks_list)
        self.assertEqual(len(functions.tasks_list), 1)

    def test_add_task_negative(self):
        functions.tasks_list = []
        initial_length = len(functions.tasks_list)
        with unittest.mock.patch('builtins.input', return_value='Test Task'):
            functions.add_task(functions.tasks_list)
        self.assertNotEqual(len(functions.tasks_list), initial_length)

    def test_add_task_input_uppercase(self):
        functions.tasks_list = []
        task = "test task"
        expected_task = "TEST TASK"
        with unittest.mock.patch('builtins.input', return_value=task):
            functions.add_task(functions.tasks_list)
        self.assertIn(expected_task, functions.tasks_list)

    def test_add_task_input_strip(self):
        functions.tasks_list = []
        task = "  test task  "
        expected_task = "TEST TASK"
        with unittest.mock.patch('builtins.input', return_value=task):
            functions.add_task(functions.tasks_list)
        self.assertIn(expected_task, functions.tasks_list)


if __name__ == '__main__':
    unittest.main()