# polymorphism_demo.py

import math

class Shape:
    """Base class for shapes with a generic area method."""

    def area(self):
        """Must be overridden by subclasses."""
        raise NotImplementedError("Subclasses must implement the area method.")


class Rectangle(Shape):
    """Rectangle shape class inheriting from Shape."""

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        """Return the area of the rectangle."""
        return self.length * self.width


class Circle(Shape):
    """Circle shape class inheriting from Shape."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Return the area of the circle."""
        return math.pi * (self.radius ** 2)
