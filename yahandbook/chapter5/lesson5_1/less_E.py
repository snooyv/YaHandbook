# E Классный прямоугольник
import math


class Rectangle:

    def __init__(self, tuple1, tuple2):
        self.ax, self.ay = tuple1
        self.cx, self.cy = tuple2

    def perimeter(self):
        ab = self.light(self.ax, self.ay, self.ax, self.cy)
        bc = self.light(self.ax, self.cy, self.cx, self.cy)
        return f"{2 * (ab + bc):.2f}"

    @staticmethod
    def light(p1x, p1y, p2x, p2y):
        dx = p1x - p2x
        dy = p1y - p2y
        return math.hypot(dx, dy)

    def area(self):
        ab = self.light(self.ax, self.ay, self.ax, self.cy)
        bc = self.light(self.ax, self.cy, self.cx, self.cy)
        return f"{ab * bc:.2f}"
