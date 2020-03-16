class Shapes:

    def __init__(self):
        self.side = 5
        self.length = 10
        self.breadth = 15

    def square(self):
        print("Area of Square:", self.side * 2)
        print("Perimeter of square:", self.side * 4)

    def rectangle(self):
        print("Area of Rectangle: ", (self.length * self.breadth))
        print("Perimeter of rectangle: ", 2 * (self.length + self.breadth))

# Calling the functions
call = Shapes()
call.square()
call.rectangle()
