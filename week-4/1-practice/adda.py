ag = "kuty"

def adda(word):
    return str(word) + "a"

ag = adda(ag)

print(ag)

ag2 = ["rep", "macsk", "cic", "alm", "Ann", "kacs"]

for i in range(len(ag2)):
    ag2[i] = adda(ag2[i])

print(ag2)
