# Padawan's attempt:

def wordcount(filename):
    original_file = open(filename + ".txt", "r")
    text = original_file.read()
    number_of_lines = text.count("\n")
    number_of_chars = len(text)
    result = [number_of_lines, number_of_chars]
    print(result)

wordcount("alma")

# Sensei's solution:

def wc(filename):
    input_file = open(filename)
    file_content = input_file.read()
    line_count = len(file_content.split("\n"))
    input_file.close()
    return [line_count, len(file_content)]

print(wc("alma.txt"))
