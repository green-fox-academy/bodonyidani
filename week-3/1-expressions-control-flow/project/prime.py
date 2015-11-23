number = 104729

sqroot = number ** 0.5

distance = int(round(sqroot - 0)) + 1

list = list(range(2, distance))

is_prime = True

for i in list:
    if number % i == 0:
        is_prime = False
        break

print(is_prime)
