original_file = open("./texts/reversed_zen_lines.txt", "r")

original = original_file.readlines()

output = ""

for line in original:
    output = output + line[::-1]
    print(output)

original_file.close()
