class Car:
    def __init__(self, color, car_type, km):
        self.color = color
        self.type = car_type
        self.km = km

    def ride(self, km):
        self.km += km


tesla = Car("pink", "Tesla S", 1200)

tesla.ride(220)

print(tesla.km)
