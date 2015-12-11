PlayingField = [[1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                [0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
                [0, 1, 0, 0, 0, 0, 0, 0, 1, 1],
                [0, 1, 0, 1, 1, 1, 1, 0, 1, 1],
                [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

def display_playing_field():
    for row in PlayingField:
        print([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

def print_user_menu():
    field = display_playing_field()
    userinput = input("\nEnter a column and row number: ")
    valid_columns = ["a", "b", "c", "d", "e", "f", "g", "h"]
    valid_rows = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    if userinput[0] not in valid_columns:
        print("Please choose a column between A and H.")
    elif userinput[1] not in valid_rows:
        print("Please choose a number between 1 and 10.")
    elif len(userinput) > 2 and int(userinput[2]) > 0:
        print("Please choose a number between 1 and 10.")
    else:
        return userinput

print_user_menu()
