#VERSION 1

new_game_submenu_name = skulls
new_game_submenu_items = "1. Re-enter Name (R)\n" + "2. Continue (C)\n" + "3. Save (S)\n" + "4. Quit (Q)\n"
new_game_submenu_input_prompt = "Please choose from the options above: "

new_game_submenu = Menu(new_game_submenu_name, new_game_submenu_items, new_game_submenu_input_prompt)
new_game_submenu_valid_inputs = ["R", "C", "S", "Q"]
new_game_submenu_error_message = skulls + " FATAL ERROR " + skulls

def run_new_game_submenu():
    Menu.print_menu(new_game_submenu)
    userinput = Menu.store_selection(new_game_submenu)
    if userinput not in new_game_submenu_valid_inputs:
        print(new_game_submenu_error_message)
        return run_new_game_submenu()
    elif userinput == "R":
        return request_username()
    elif userinput == "C":
        return roll_stats()
    elif userinput == "S":
        return run_save_submenu()
    elif userinput == "Q":
        return run_quit_submenu()


#VERSION 2

def run_new_game_submenu():
    new_game_submenu.print_menu()
    userinput = new_game_submenu.store_selection()
    if userinput not in new_game_submenu.valid_inputs():
        print_error_message()
        return run_new_game_submenu()
    else:
        return new_game_submenu.choose(userinput)

new_game_submenu = Menu("start game", [
    MenuItem("r", "re-enter name", request_username),
    MenuItem("c", "continue", roll_stats),
    MenuItem("s", "save", run_save_submenu),
    MenuItem("q", "quit", run_quit_submenu)
    ],
    "Choose from the options above: ")
