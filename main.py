"""Shape"""
from abc import ABC, abstractmethod


class Shape(ABC):
    """abstract"""
    @abstractmethod
    def area(self):
        """area"""
        pass


class Rectangle(Shape):
    """rectangle"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width


class Circle(Shape):
    """circle"""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2


rectangle = Rectangle(5, 6)
circle = Circle(5)

print(rectangle.area())
print(circle.area())
