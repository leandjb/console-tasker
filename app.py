import functions

if __name__ == "__main__":
    while True:

        # menu
        print("\n--- TASKER CLI ---\n")
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task as completed")
        print("4. Remove task")
        print("5. Exit")

        # input
        try:
            option = int(input("\n> Choose an option: \n"))
        except ValueError:
            print("\n*** INVALID OPTION ***\n")
            continue

        match option:
            case 1:
                functions.add_task(functions.todo_tasks)

            case 2:
                functions.view_tasks(functions.todo_tasks)

            case 3:
                functions.mark_as_completed(functions.todo_tasks)

            case 4:
                functions.remove_task(functions.todo_tasks)

            case 5:
                print("\n*** EXITING ***\n")
                break

            case _:
                print("\n*** INVALID OPTION ***\n")
