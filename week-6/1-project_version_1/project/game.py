from random import randint
import unicodedata

class Menu():
    def __init__(self, menu_name, menu_items, input_prompt):
        self.menu_name = menu_name
        self.menu_items = menu_items
        self.input_prompt = input_prompt

    def print_menu(self):
        print(self.menu_name)
        print(self.menu_items)

    def store_selection(self):
        selection = input(self.input_prompt)
        return selection.upper()

class Player():
    def __init__(self = None, name = None, dexterity = None, health = None, luck = None, inventory = ["Sword", "Leather Armor"]):
        self.name = name
        self.dexterity = dexterity
        self.health = health
        self.luck = luck
        self.inventory = inventory

    def store_name(self, name):
        self.name = name

    def store_initial_dexterity_health_luck(self, dexterity, health, luck):
        self.dexterity = dexterity
        self.health = health
        self.luck = luck

    def store_potion(self, potion):
        self.inventory = [self.inventory[0], self.inventory[1]]
        self.inventory.append(potion)

player = Player()

skulls = "\n\n"+ (unicodedata.lookup("skull") + " ") * 30 + "\n\n"

main_menu_name = skulls + " MAIN MENU " + skulls
main_menu_items = "1. New Game (N)\n" + "2. Load Game (G)\n" + "3. Exit (E)\n"
main_menu_input_prompt = "Choose from the options above: "

main_menu = Menu(main_menu_name, main_menu_items, main_menu_input_prompt)
main_menu_valid_inputs = ["N", "G", "E"]
main_menu_error_message = skulls + " FATAL ERROR " + skulls

def run_main_menu():
    Menu.print_menu(main_menu)
    userinput = Menu.store_selection(main_menu)
    if userinput not in main_menu_valid_inputs:
        print(main_menu_error_message)
        return run_main_menu()
    elif userinput == "N":
        return request_username()

def request_username():
    username = input(skulls + "Enter your name, Mortal: ")
    print(skulls + " Welcome " + username + "!")
    player.store_name(username)
    return run_new_game_submenu()

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
    elif userinput == "Q":
        return run_quit_submenu()

quit_submenu_name = skulls
quit_submenu_items = "1. Save & Quit (S)\n" + "2. Quit without Saving (Q)\n" + "3. Resume (R)\n"
quit_submenu_input_prompt = "Please choose from the options above: "

quit_submenu = Menu(quit_submenu_name, quit_submenu_items, quit_submenu_input_prompt)
quit_submenu_valid_inputs = ["S", "Q", "R"]
quit_submenu_error_message = skulls + " FATAL ERROR " + skulls

def run_quit_submenu():
    Menu.print_menu(quit_submenu)
    userinput = Menu.store_selection(quit_submenu)
    if userinput not in quit_submenu_valid_inputs:
        print(quit_submenu_error_message)
        return run_quit_submenu()
    elif userinput == "R":
        return run_new_game_submenu()

def roll_stats():
    dexterity_dice = randint(1, 6)
    dexterity_value = dexterity_dice + 6
    health_dice = randint(2, 12)
    health_value = health_dice + 12
    luck_dice = randint(1, 6)
    luck_value = luck_dice + 6
    message = skulls + " Welcome to the Labyrinth of Death! Fate has decided that you shall have:" + skulls
    display_dexterity = " Dexterity: " + str(dexterity_value) + "\n"
    display_health = " Health: " + str(health_value) + "\n"
    display_luck = " Luck: " + str(luck_value) + "\n"
    print(message + display_dexterity + display_health + display_luck)
    player.store_initial_dexterity_health_luck(dexterity_value, health_value, luck_value)
    return run_roll_stats_submenu()

roll_stats_submenu_name = skulls
roll_stats_submenu_items = "1. Re-roll Stats (R)\n" + "2. Continue (C)\n" + "3. Save (S)\n" + "4. Quit (Q)\n"
roll_stats_submenu_input_prompt = "Please choose from the options above: "

roll_stats_submenu = Menu(roll_stats_submenu_name, roll_stats_submenu_items, roll_stats_submenu_input_prompt)
roll_stats_submenu_valid_inputs = ["R", "C", "S", "Q"]
roll_stats_submenu_error_message = skulls + " FATAL ERROR " + skulls

def run_roll_stats_submenu():
    Menu.print_menu(roll_stats_submenu)
    userinput = Menu.store_selection(roll_stats_submenu)
    if userinput not in roll_stats_submenu_valid_inputs:
        print(roll_stats_submenu_error_message)
        return run_roll_stats_submenu()
    elif userinput == "R":
        return roll_stats()
    elif userinput == "C":
        return run_select_potion_submenu()

select_potion_submenu_name = skulls
select_potion_submenu_items = "1. Potion of Dexterity (D)\n" + "2. Potion of Health (H)\n" + "3. Potion of Luck (L)\n"
select_potion_submenu_input_prompt = "Choose your poison: "

select_potion_submenu = Menu(select_potion_submenu_name, select_potion_submenu_items, select_potion_submenu_input_prompt)
select_potion_submenu_valid_inputs = ["D", "H", "L"]
select_potion_submenu_error_message = skulls + " FATAL ERROR " + skulls

def run_select_potion_submenu():
    Menu.print_menu(select_potion_submenu)
    userinput = Menu.store_selection(select_potion_submenu)
    if userinput not in select_potion_submenu_valid_inputs:
        print(select_potion_submenu_error_message)
        return run_select_potion_submenu()
    elif userinput == "D":
        print(skulls + "You have selected the Potion of Dexterity. Are you sure you don't want to change your mind?" + skulls)
        player.store_potion("Potion of Dexterity")
        return run_reselect_potion_submenu()
    elif userinput == "H":
        print(skulls + "You have selected the Potion of Health. Are you sure you don't want to change your mind?" + skulls)
        player.store_potion("Potion of Health")
        return run_reselect_potion_submenu()
    elif userinput == "L":
        print(skulls + "You have selected the Potion of Luck. Are you sure you don't want to change your mind?" + skulls)
        player.store_potion("Potion of Luck")
        return run_reselect_potion_submenu()

reselect_potion_submenu_name = ""
reselect_potion_submenu_items = "1. Re-select Potion (R)\n" + "2. Continue (C)\n" + "3. Quit (Q)\n"
reselect_potion_submenu_input_prompt = "Please choose from the options above: "

reselect_potion_submenu = Menu(reselect_potion_submenu_name, reselect_potion_submenu_items, reselect_potion_submenu_input_prompt)
reselect_potion_submenu_valid_inputs = ["R", "C", "Q"]
reselect_potion_submenu_error_message = skulls + " FATAL ERROR " + skulls

def run_reselect_potion_submenu():
    Menu.print_menu(reselect_potion_submenu)
    userinput = Menu.store_selection(reselect_potion_submenu)
    if userinput not in reselect_potion_submenu_valid_inputs:
        print(reselect_potion_submenu_error_message)
        return run_reselect_potion_submenu()
    elif userinput == "R":
        return run_select_potion_submenu()
    elif userinput == "C":
        return print_character()

def print_character():
    print(skulls)
    print("NAME: " + str(player.name))
    print("DEXTERITY: " + str(player.dexterity))
    print("HEALTH: " + str(player.health))
    print("LUCK: " + str(player.luck))
    print("YOU HAVE: " + player.inventory[0] + ", " + player.inventory[1] + ", " + player.inventory[2])
    print(skulls)

run_main_menu()
