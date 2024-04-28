import funciones

# mainloop
while True:

    # menu
    print("\n*** TASKER ***\n")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Remove task")
    print("5. Exit")

    #input
    option = int(input("\n> Choose an option: \n"))

    match option:
        case 1:
            funciones.add_task()
        case 2:
            funciones.view_tasks()
        case 3:
            funciones.mark_as_completed()
        case 4:
            funciones.remove_task()
        case 5:
            print("\n*** GOOD BYE ***\n")
            break
        case _:
            print("\n*** INVALID OPTION ***\n")
