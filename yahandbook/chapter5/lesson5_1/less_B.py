#  Классная точка  2.0
import math


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def length(self, p):
        dx = self.x - p.x
        dy = self.y - p.y
        return f"{math.hypot(dx, dy):.2f}"
