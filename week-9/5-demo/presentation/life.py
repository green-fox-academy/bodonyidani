class Octopus():
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        print(self.__name)

    def meet(self, other):
        print(self.__name + " meets " + other.name)


class Snake():
    def __init__(self, name):
        self.name = name

    def get_name(self):
        print(self.name)

    def meet(self, other):
        print(self.name + " meets " + other.__name)

octopus = Octopus("Paul the Psychic Octopus")
snake = Snake("Professor Snape")

octopus.get_name()
snake.get_name()

#snake.meet(octopus)

#octopus.meet(snake)
