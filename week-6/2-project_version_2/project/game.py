from display import print_skulls, print_error_message
from menu import MenuItem, Menu
from player import Player
from random import randint
import unicodedata

player = Player()

def run_main_menu():
    main_menu.print_menu()
    userinput = main_menu.store_selection()
    if userinput not in main_menu.valid_inputs():
        print_error_message()
        return run_main_menu()
    else:
        return main_menu.choose(userinput)

def request_username():
    print_skulls()
    username = input("ENTER YOUR NAME, MORTAL: ")
    print_skulls()
    print(" WELCOME " + username.upper() + "!")
    player.set_name(username)
    return run_new_game_submenu()

def run_new_game_submenu():
    new_game_submenu.print_menu()
    userinput = new_game_submenu.store_selection()
    if userinput not in new_game_submenu.valid_inputs():
        print_error_message()
        return run_new_game_submenu()
    else:
        return new_game_submenu.choose(userinput)

def run_roll_stats_submenu():
    roll_stats_submenu.print_menu()
    userinput = roll_stats_submenu.store_selection()
    if userinput not in roll_stats_submenu.valid_inputs():
        print_error_message()
        return run_roll_stats_submenu()
    else:
        return roll_stats_submenu.choose(userinput)

def roll_stats():
    roll_dice = randint(1, 6)
    dexterity_value = roll_dice + 6
    roll_two_dices = randint(2, 12)
    health_value = roll_two_dices + 12
    roll_dice = randint(1, 6)
    luck_value = roll_dice + 6
    print_skulls()
    print(" Welcome to the Labyrinth of Death! Fate has decided that you shall have:")
    print_skulls()
    player.set_initial_dexterity_health_luck(dexterity_value, health_value, luck_value)
    player.display_stats()
    return run_roll_stats_submenu()

def run_select_potion_submenu():
    select_potion_submenu.print_menu()
    userinput = select_potion_submenu.store_selection()
    if userinput not in select_potion_submenu.valid_inputs():
        print_error_message()
        return run_select_potion_submenu()
    else:
        if userinput == "D":
            player.set_potion("POTION OF DEXTERITY")
        elif userinput == "H":
            player.set_potion("POTION OF HEALTH")
        elif userinput == "L":
            player.set_potion("POTION OF LUCK")
        print_skulls()
        print("Are you sure you don't want to change your mind?")
        print_skulls()
        return select_potion_submenu.choose(userinput)

def run_reselect_potion_submenu():
    reselect_potion_submenu.print_menu()
    userinput = reselect_potion_submenu.store_selection()
    if userinput not in reselect_potion_submenu.valid_inputs():
        print_error_message()
        return run_reselect_potion_submenu()
    else:
        return reselect_potion_submenu.choose(userinput)

main_menu = Menu("main menu", [
    MenuItem("n", "new game", request_username),
    MenuItem("l", "load game", "load_game"),
    MenuItem("e", "exit", "exit_game")
    ],
    "Choose from the options above: ")

new_game_submenu = Menu("start game", [
    MenuItem("r", "re-enter name", request_username),
    MenuItem("c", "continue", roll_stats),
    MenuItem("s", "save", "save"),
    MenuItem("q", "quit", "quit")
    ],
    "Choose from the options above: ")

roll_stats_submenu = Menu("roll again or go further", [
    MenuItem("r", "re-roll stats", roll_stats),
    MenuItem("c", "continue", run_select_potion_submenu),
    MenuItem("s", "save", "save"),
    MenuItem("q", "quit", "quit")
    ],
    "Choose from the options above: ")

select_potion_submenu = Menu("choose a potion", [
    MenuItem("d", "potion of dexterity", run_reselect_potion_submenu),
    MenuItem("h", "potion of health", run_reselect_potion_submenu),
    MenuItem("l", "potion of luck", run_reselect_potion_submenu)
    ],
    "Choose your poison: ")

reselect_potion_submenu = Menu("are you ready?", [
    MenuItem("r", "re-select potion", run_select_potion_submenu),
    MenuItem("c", "continue", player.print_character),
    MenuItem("q", "quit", "quit")
    ],
    "Choose from the options above: ")

run_main_menu()
