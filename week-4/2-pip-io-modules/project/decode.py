original_file = open("./texts/zen_of_python.txt", "r")
encoded_file = open("./texts/encoded_zen_lines.txt", "r")

original = original_file.read()
encoded = encoded_file.read()

code = ord(original[0]) - ord(encoded[0])

output = ""

i = 0

while i < len(encoded):
    if encoded[i] == " " or encoded[i] == "\n":
        output += encoded[i]
    else:
        output += chr(ord(encoded[i]) + code)
    i += 1

print(output)

original_file.close()
encoded_file.close()
