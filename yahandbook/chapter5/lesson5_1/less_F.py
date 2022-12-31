# Классный прямоугольник 2.0
import math


class Rectangle:

    def __init__(self, tuple1, tuple2):
        self.ax, self.ay = tuple1
        self.cx, self.cy = tuple2

    def chek_conrner(self):
        if self.ax < self.cx:
            self.ax, self.ay = self.cx, self.cy

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

    def get_pos(self):
        return round(self.ax, 2), round(self.cy, 2)

    def get_size(self):
        ab = self.light(self.ax, self.ay, self.ax, self.cy)
        bc = self.light(self.ax, self.cy, self.cx, self.cy)
        return round(bc, 2), round(ab, 2)

    def move(self, dx, dy):
        self.ax += dx
        self.ay += dy
        self.cx += dx
        self.cy += dy

    def resize(self, width, height):
        self.ax -= height
        self.cy -= width
