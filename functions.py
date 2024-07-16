"""
Archivo con las funciones para hacer CRUD [Crear, ver, modificar y  borrar] de
actividades en el gestor de tareas
"""
tasks_list: list = []


def add_task(input_list: list):
    """
    funcion para adicionar tarear en una lista.
    """
    task = input(" > Enter task:").capitalize().strip()
    input_list.append(task)
    print("*** TASK ADDED ***", end="\n")


def view_tasks(input_list: list):
    if len(input_list) == 0:
        print("*** NO TASKS ADDED ***", end="\n")

    if len(input_list) > 0:
        print("++++ LIST OF TASKS ++++", end="\n")

        for todo_task in input_list:
            print(f"[{input_list.index(todo_task) + 1}] {todo_task}", end="\n")
        print("+++ END LIST OF TASK +++", end="\n")


def mark_task(input_list: list):
    """
    Función para marcar una tarea como completada en una lista de tareas.
    """
    if len(input_list) == 0:
        print("*** NO TASKS ADDED ***", end="\n")

    if len(input_list) > 0:
        print("+++ TASKS +++", end="\n")

        for task in input_list:
            print(f"[{input_list.index(task) + 1}] {task}", end="\n")

        try:
            task_to_complete = int(
                input(" > Choose a task to mark as completed:"))

        except ValueError:
            print("\n*** INVALID OPTION ***", end="\n")
            return


def remove_task(input_list: list):
    if input_list:
        view_tasks(input_list)

        task = int(input(" > Enter index task to delete: "))

        if task <= 0 or task > len(input_list):
            print("\n*** INVALID OPTION ***", end="\n")
        else:
            del input_list[task - 1]
            print("*** TASKS DELETED ***", end="\n")


    else:
        print("*** NO TASKS ADDED ***", end="\n")
