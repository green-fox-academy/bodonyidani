def multiply(a, b):
    return a * b

def test(expected, actual, message):
    if expected == actual:
        print("Check")
    else:
        print(message)

test(multiply(1,2), 3, "it should multiply numbers")
