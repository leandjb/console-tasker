todo_tasks = []


def add_task(todo_list: list):
    # Entrada para la tarea
    todo_task = input("\n> Enter task: ")

    # Añadir la tarea al final de la lista
    todo_list.append(todo_task)

    # Informe de tarea añadida
    print("\n*** TASK ADDED ***\n")
    print(f"{todo_task} [{len(todo_list)}]\n")


def view_tasks(todo_list: list):
    #ver lista de tareas
    if len(todo_list) == 0:
        print("\n*** NO TASKS ADDED ***\n")
    if len(todo_list) > 0:
        print("\n*** TASKS ***\n")
        for task in todo_list:
            print(f"{task} [{todo_list.index(task) + 1}]")
        print("\n")


def mark_as_completed(todo_list: list):
    if len(todo_list) == 0:
        print("\n*** NO TASKS ADDED ***\n")
    if len(todo_list) > 0:
        print("\n*** TASKS ***\n")
        for task in todo_list:
            print(f"{task} [{todo_list.index(task) + 1}]")
        print("\n")
        try:
            task_to_complete = int(
                input("\n> Choose a task to mark as completed: \n"))
        except ValueError:
            print("\n*** INVALID OPTION ***\n")
            return


def remove_task(todo_list: list):
    if len(todo_list) == 0:
        print("\n*** NO TASKS ADDED ***\n")
    if len(todo_list) > 0:
        print("\n*** TASKS ***\n")
        for task in todo_list:
            print(f"{task} [{todo_list.index(task) + 1}]")
        print("\n")
        try:
            task_to_remove = int(input("\n> Choose a task to remove: \n"))
        except ValueError:
            print("\n*** INVALID OPTION ***\n")
            return
