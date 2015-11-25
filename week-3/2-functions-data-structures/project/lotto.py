import db

data = db.data()

num_list_all = []

for i in data:
    num_list_all += i[11:16]

test = [[x,num_list_all.count(x)] for x in set(num_list_all)]

print(test)
