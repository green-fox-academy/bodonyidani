def count_letters(input_str):
    output = {}
    for i in input_str:
        output[i] = input_str.count(i)
    return output
