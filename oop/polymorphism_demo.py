
import math

class Shape:
    def area(self):
        """
        Base method to be overridden by derived classes
        """
        raise NotImplementedError("Subclasses must implement this method")


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """
        Calculates area of a rectangle
        """
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """
        Calculates area of a circle
        """
        return math.pi * (self.radius ** 2)
