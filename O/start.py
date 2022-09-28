import math
from typing import List


class Rect:
    def __init__(self, width, height):
        self.width = width
        self.height = height


class Circle:
    def __init__(self, radius):
        self.radius = radius


class AreaCalculator:
    def __init__(self, shapes: List[Rect]):
        self.shapes = shapes

    def total_area(self) -> float:
        sum = 0
        for el in self.shapes:
            if isinstance(el, Rect):
                sum += el.width * el.height
            if isinstance(el, Circle):
                sum += math.pi * el.radius ** 2
        return sum


ar_sh = AreaCalculator([Rect(10, 10), Rect(4, 5), Rect(3, 3)])

