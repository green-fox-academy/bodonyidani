from random import randint

def get_integer():
    number = int(input("Enter an integer: "))
    return number

number_to_guess = randint(0, 10)

number_of_guesses = 5

while number_of_guesses > 0:
    try:
        guess = get_integer()
    except ValueError:
        print("I said integer! Try again, mate.")
    else:
        if guess == number_to_guess:
            print("Bingo!")
            break
        elif guess < number_to_guess:
            number_of_guesses -= 1
            print("No luck this time, mine's bigger, buddy. Try again.")
        else:
            number_of_guesses -= 1
            print("No luck this time, you're aiming too high. Try again.")
