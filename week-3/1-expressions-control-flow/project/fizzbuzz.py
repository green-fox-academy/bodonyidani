number = 0

while number <= 100:
    if number % 3 == 0 and number % 5 == 0 or "5" in str(number) and "3" in str(number) or number % 3 == 0 and "5" in str(number) or number % 5 == 0 and "3" in str(number):
        print("FIZZBUZZ")
    elif number % 3 == 0 or "3" in str(number):
        print("FIZZ")
    elif number % 5 == 0 or "5" in str(number):
        print("BUZZ")
    else:
        print(number)
    number += 1
