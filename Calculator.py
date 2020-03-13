class Add:
    num_1 = 1
    num_2 = 2

    def __init__(self):
        self.num_1 = 5
        self.num_2 = 10

    def calculate(self):
        print("number 1 = ", self.num_1)
        print("number 2 = ", self.num_2)

        initial_sum = self.num_1 + self.num_2
        print("Sum  is ", initial_sum)

        print("Working on it for the second time")
        print("number 1 = ", Add.num_1)
        print("number 2 = ", Add.num_2)

        class_sum = Add.num_1 + Add.num_2
        print("Sum is", class_sum)


calc = Add()
calc.calculate()
