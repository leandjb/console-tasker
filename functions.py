todo_tasks: list = []


def add_task(todo_list: list):
    todo_task = input("> Enter task:")
    todo_list.append(todo_task)

    print("*** TASK ADDED ***", end="\n")
    print(f"{todo_task} [{len(todo_list)}]", end="\n\n")


def view_tasks(todo_list: list):
    if len(todo_list) == 0:
        print("\n*** NO TASKS ADDED ***", end="\n\n")

    if len(todo_list) > 0:
        print("+++ TASKS SAVED +++", end="\n")
        for task in todo_list:
            print(f"[{todo_list.index(task) + 1}] {task}", end="\n")
        print("+++++++ END +++++++", end="\n\n")


def mark_task(todo_list: list):
    if len(todo_list) == 0:
        print("\n*** NO TASKS ADDED ***", end="\n")

    if len(todo_list) > 0:
        print("+++ TASKS +++", end="\n")
        for task in todo_list:
            print(f"[{todo_list.index(task) + 1}] {task}", end="\n")
        print("\n")
        try:
            task_to_complete = int(
                input("> Choose a task to mark as completed:", end="\n"))
        except ValueError:
            print("\n*** INVALID OPTION ***", end="\n")
            return


def remove_task(todo_list: list):
    if len(todo_list) == 0:
        print("\n*** NO TASKS ADDED ***", end="\n")

    if len(todo_list) > 0:
        print("+++ TASKS +++", end="\n")
        for task in todo_list:
            print(f"[{todo_list.index(task) + 1}] {task}", end="\n")

        try:
            task_to_remove = int(input("> Choose a task to remove:", end="\n"))
        except ValueError:
            print("\n*** INVALID OPTION ***", end="\n")
            return
