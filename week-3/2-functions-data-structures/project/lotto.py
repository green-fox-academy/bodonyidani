import db

data = db.data()

num_list_all = []

for i in data:
    num_list_all += i[11:16]

dictionary = {x:num_list_all.count(x) for x in num_list_all}

times_drawn = [num_list_all.count(x) for x in dictionary]

reverse_list = sorted(dictionary, key=dictionary.get)

reverse_list.reverse()

print(reverse_list[0:5])

import matplotlib.pyplot as plt

colors = list("rgbcmyk")

plt.figure(1)
plt.hist(num_list_all, bins=90, histtype="stepfilled", color = "y", alpha = 0.5)
plt.title("Lottery Numbers")
plt.xlabel("Balls")
plt.ylabel("Times Drawn")

plt.show()

plt.figure(2)
plt.hist(times_drawn, bins=9, histtype="stepfilled", color = "b")
plt.title("Lottery Numbers Distribution")
plt.xlabel("Times Drawn")
plt.ylabel("Number Of Balls")

plt.show()
