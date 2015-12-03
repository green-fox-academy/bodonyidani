def run_app():
    task_file = open("task_list.txt", "r")
    task_file_content = task_file.read()
    task_list = task_file_content.split("\n")
    task_file.close()
    main_menu_choice = run_main_menu()
    while main_menu_choice.upper() != "Q":
        if main_menu_choice.upper() == "A":
            new_task = input("Add a new task: ")
            task_list.insert(len(task_list) - 1,new_task)
            main_menu_choice = run_main_menu()
        elif main_menu_choice.upper() == "R":
            i = 0
            while i < len(task_list) - 1:
                print(str(i + 1) + ": " + task_list[i])
                i += 1
            removal_index = input("Enter the number of the task you'd like to remove: ")
            removal_index = int(removal_index)
            task_list.pop(removal_index - 1)
            main_menu_choice = run_main_menu()
    else:
        updated_task_list = ""
        for task in task_list:
            updated_task_list += str(task) + "\n"
        task_file_to_update = open("task_list.txt", "w")
        task_file_to_update.write(updated_task_list)
        task_file_to_update.close()

def run_main_menu():
    main_menu_text = "What would you like to do?\n" + "1. Add new task (A)\n" + "2. Remove task (R)\n" + "3. Quit this crap (Q)\n"
    print(main_menu_text)
    main_menu_choice = input("Enter your choice: ")
    return main_menu_choice

run_app()
