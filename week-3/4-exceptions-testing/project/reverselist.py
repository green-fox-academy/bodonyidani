def reverse(in_list):
    reverselist = []
    i = len(in_list) - 1
    while i >= 0:
         reverselist.append(in_list[i])
         i -= 1
    return reverselist

output = reverse([1, 2, 3, 4])
print(output)
