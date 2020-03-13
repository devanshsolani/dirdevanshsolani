from abc import ABC
import math


# Abstract Class  
class Shape(ABC):

    # Abstract method
    def no_of_sides(self):
        pass

    # Abstract method
    def calculate_area(self):
        pass

    # Abstract method
    def calculate_perimeter(self):
        pass


class Rectangle(Shape):

    # Overriding abstract method
    def no_of_sides(self, length, breadth):
        print("Length = 40\nBreadth = 30")
        self.length = length
        self.breadth = breadth

    # Overriding abstract method
    def calculate_area(self):
        print("Area of Rectangle: ", self.length*self.breadth)

    # Overriding abstract method
    def calculate_perimeter(self):
        print("Perimeter of Rectangle: ", 2 * (self.length+self.breadth), "\n")


class Square(Shape):

    # Overriding abstract method
    def no_of_sides(self, side):
        print("Side = 10")
        self.side = side

    # Overriding abstract method
    def calculate_area(self):
        print("Area of Square: ", self.side**2)

    # Overriding abstract method
    def calculate_perimeter(self):
        print("Perimeter of Square: ", 4 * self.side, "\n")


class Circle(Shape):

    # Overriding abstract method
    def no_of_sides(self, radius):
        print("Radius = 7")
        self.radius = radius

    # Overriding abstract method
    def calculate_area(self):
        print("Area of Circle: ", (22/7) * self.radius ** 2)

    # Overriding abstract method
    def calculate_perimeter(self):
        print("Perimeter of Circle: ", 2 * (22/7) * self.radius, "\n")


class Ellipse(Shape):

    # Overriding abstract method
    def no_of_sides(self, semiMajorAxis, semiMinorAxis):
        print("Semi Major Axis = 2\nSemi Major Axis = 2")
        self.semiMajorAxis = semiMajorAxis
        self.semiMinorAxis = semiMinorAxis

    # Overriding abstract method
    def calculate_area(self):
        print("Area of Ellipse: ", (22/7) * self.semiMajorAxis * self.semiMinorAxis)

    # Overriding abstract method
    def calculate_perimeter(self):
        print("Perimeter of Ellipse: ", 2 * (22/7) ** math.sqrt((self.semiMajorAxis +
                                                                 self.semiMinorAxis)/ 2))


objRect = Rectangle()
objRect.no_of_sides(40, 30)
objRect.calculate_area()
objRect.calculate_perimeter()

objSquare = Square()
objSquare.no_of_sides(10)
objSquare.calculate_area()
objSquare.calculate_perimeter()

objCircle = Circle()
objCircle.no_of_sides(7)
objCircle.calculate_area()
objCircle.calculate_perimeter()

objEllipse = Ellipse()
objEllipse.no_of_sides(2, 2)
objEllipse.calculate_area()
objEllipse.calculate_perimeter()
