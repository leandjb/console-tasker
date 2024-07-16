import unittest

class TestRemoveTask(unittest.TestCase):

    def test_remove_task_no_tasks_added(self):
        todo_list = []
        with self.assertRaises(SystemExit):
            remove_task(todo_list)

    def test_remove_task_with_tasks(self):
        todo_list = ['Task 1', 'Task 2', 'Task 3']
        with unittest.mock.patch('builtins.input', return_value='2'):
            remove_task(todo_list)
            self.assertNotIn('Task 2', todo_list)

    def test_remove_task_invalid_option(self):
        todo_list = ['Task 1', 'Task 2', 'Task 3']
        with unittest.mock.patch('builtins.input', return_value='invalid'):
            with self.assertRaises(SystemExit):
                remove_task(todo_list)

if __name__ == '__main__':
    unittest.main()
