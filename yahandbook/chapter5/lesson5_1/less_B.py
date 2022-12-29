#  Классная точка  2.0
import math


class Point:

    def __init__(self, x, y, l=0):
        self.x = x
        self.y = y
        self.l = l

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def length(self, p):
        dx = self.x - p.x
        dy = self.y - p.y
        self.l = math.hypot(dx, dy)
        return self.l

    # @property
    # def __str__(self):
    #     return '(Point {0})'.format(self.l)
