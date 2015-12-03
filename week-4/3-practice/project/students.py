students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5},
        {'name': 'Olaf', 'age': 12, 'candies': 7},
        {'name': 'Teodor', 'age': 3, 'candies': 2}
]

def find_rich_students(list):
    count = 0
    for item in list:
        if item["candies"] > 4:
            count +=1
    return count

print(find_rich_students(students))

#With filter:

def is_rich(student):
    return student["candies"] > 4

def filter_rich_kids(kidlist):
    return len(list(filter(is_rich, kidlist)))

print(filter_rich_kids(students))
