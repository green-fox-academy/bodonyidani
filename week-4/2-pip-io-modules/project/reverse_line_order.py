original_file = open("./texts/reversed_zen_order.txt", "r")

output_list = original_file.readlines()[::-1]

for line in output_list:
    print(line.rstrip())

original_file.close()
