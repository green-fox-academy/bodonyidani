n = 5

def factorial(n):
    numbers = list(range(1, n + 1))
    result = 1
    for i in numbers:
        result = result * i
    return result

print(factorial(n))

x = 6

def factorialr(n):
    if n == 1:
        return 1
    else:
        return factorialr(n - 1) * n

print(factorialr(x))
