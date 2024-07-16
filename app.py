from functions import tasks_list, add_task, view_tasks, mark_task, remove_task

if __name__ == "__main__":
    while True:

        # menu
        print("--- TASKER MENU ---", end="\n", flush=True)
        print("1. Add task")
        print("2. View tasks")
        print("3. Mark task")
        print("4. Remove task")
        print("5. Exit", end="\n")

        # input selection option
        try:
            option = int(input(" > Choose an option:"))
        except ValueError:
            print("*** INVALID OPTION ***", end="\n")
            continue

        match option:
            case 1:
                add_task(tasks_list)

            case 2:
                view_tasks(tasks_list)

            case 3:
                mark_task(tasks_list)

            case 4:
                remove_task(tasks_list)

            case 5:
                print("*** EXITING ***", end="\n")
                break

            case _:
                print("*** INVALID OPTION ***", end="\n")
                print(" > Please, try again.", end="\n")
