import random
from colorama import Fore, Back, Style

print("PROFESSOR SNAKE SAYZZZZZ")

def get_string():
    userinput = input(Fore.GREEN + "Sssay sssomething: ")
    return userinput

snake_abuses = ["thisss isssn't Javassscript, go back to ssschool.", "I sssupose that'ss too abssstract for you.", "you thhhought that for cccycle would work?", "you sssneaky ssson of a sssnake.", "it's not indented, you demented dementor.", "your brain is smaller than a quidditch ball."]

vowels = ["a", "e", "i", "o", "u"]

def snakesays():
    if word == "" or word == " ":
        print(Fore.WHITE + "Python-schmython, " + random.choice(snake_abuses))
    elif word[0] == " " and not word[1] in vowels:
        print(Fore.WHITE + word[1].upper() + word[2:len(word)] + "-ssschm" + word[2:len(word)] + ", " + random.choice(snake_abuses))
    elif word[0] == " ":
        print(Fore.WHITE + word[1].upper() + word[2:len(word)] + "-ssschm" + word[1:len(word)] + ", " + random.choice(snake_abuses))
    else:
        snake_word = word
        i = len(word) - 1
        while i >= 0:
            snake_word = snake_word + word[i]
            i -= 1
        print(Fore.WHITE + snake_word)

number_of_tries = 8

while number_of_tries >= 0:
    word = get_string()
    snakesays()
    number_of_tries -= 1
else:
    word = get_string()
    print(Fore.WHITE + "Sssod off, I'm going to ssssleep.")
