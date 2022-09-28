import math
from typing import List
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        ...


class Rect(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * el.radius ** 2


class AreaCalculator:
    def __init__(self, shapes: List[Rect]):
        self.shapes = shapes

    def total_area(self) -> float:
        sum_ = 0
        for shape in self.shapes:
            sum_ += shape.area()
        return sum_


ar_sh = AreaCalculator([Rect(10, 10), Rect(4, 5), Rect(3, 3)])

