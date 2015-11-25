class MySuperString:
    def __init__(self, mystr):
        self.mystr = mystr

    def reverse(self):
        reversed = ""
        for i in self.mystr:
            reversed = i + reversed
        return reversed

    def charactercount(self, x):
        count = 0
        for i in self.mystr:
            if i == x:
                count += 1
        return count

    def snake_case(self):
        new_string = ""
        for i in self.mystr:
            if i == " ":
                new_string += "_"
            else:
                new_string += i
        return new_string
