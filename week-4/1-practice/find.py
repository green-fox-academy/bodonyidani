students = [
    {"name": "Tibi", "age": 8},
    {"name": "Adorjan", "age": 9},
    {"name": "Agoston", "age": 6},
    {"name": "Aurel", "age": 7},
    {"name": "Dezso", "age": 12}
]

student_names_at_least_8 = []

for item in students:
    if item["age"] >= 8:
        student_names_at_least_8.append(item["name"])

print(student_names_at_least_8)

student_ages_starting_with_A = []

for item in students:
    if item["name"][0] == "A":
        student_ages_starting_with_A.append(item["age"])

print(student_ages_starting_with_A)
