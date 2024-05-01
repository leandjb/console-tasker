import functions

if __name__ == "__main__":
    while True:

        # menu
        print("---- TASKER CLI ----", end="\n", flush=True)
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task")
        print("4. Remove task")
        print("5. Exit")
        print("--------------------")

        # input
        try:
            option = int(input("> Choose an option:"))
        except ValueError:
            print("\n*** INVALID OPTION ***", end="\n")
            continue

        match option:
            case 1:
                functions.add_task(functions.todo_tasks)

            case 2:
                functions.view_tasks(functions.todo_tasks)

            case 3:
                functions.mark_task(functions.todo_tasks)

            case 4:
                functions.remove_task(functions.todo_tasks)

            case 5:
                print("*** EXITING ***", end="\n")
                break

            case _:
                print("*** INVALID OPTION ***", end="\n")
