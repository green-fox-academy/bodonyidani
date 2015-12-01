def initCar(color, type, km):
    car = {"color": "", "type": "", "km": 0}
    car["color"] = color
    car["type"] = type
    car["km"] = km
    return car

def ride(car, km):
    car["km"] += km

tesla = initCar("pink", "Tesla S", 1200)

lada = initCar("red", "Lada 1200", 40000)

ifa = initCar("brown", "Ifa", 30000000)

ride(ifa, 220)

print(ifa)
