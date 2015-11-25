class MyMath():
    def __init__(self, num_list):
        self.num_list = num_list

    def average(self, num_list):
        sum = 0
        pop = 0
        for n in self.num_list:
            sum += n
            pop += 1
        return sum / pop
