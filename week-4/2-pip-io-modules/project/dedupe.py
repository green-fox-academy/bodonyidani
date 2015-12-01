original_file = open("./texts/duplicated_chars.txt", "r")

original = original_file.read()

output = ""

i = 0

while i < len(original):
    if original[i] == "\n":
        output += original[i]
    elif i % 2 != 0:
        output += original[i]
    i += 1

print(output)

original_file.close()
