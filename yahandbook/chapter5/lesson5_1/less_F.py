# Классный прямоугольник 2.0
import math


class Rectangle:

    def __init__(self, tuple1, tuple2):
        # self.ax, self.ay = tuple1
        # self.cx, self.cy = tuple2
        self.chek_corner2(tuple1, tuple2)

    # def chek_conrner(self, tuple1, tuple2):
    #     self.ax, self.ay = tuple1
    #     self.cx, self.cy = tuple2
    #     if self.ax < self.cx and self.ay < self.cy:
    #         print("AC")
    #         print("Новая версия")
    #         return "AC"
    #     elif self.ax < self.cx and self.ay > self.cy:
    #         print("BD")
    #         return "BD"
    #     elif self.ay < self.cy:
    #         print("DB")
    #         return "DB"
    #     print("CA")
    #     return "CA"

    @staticmethod
    def chek_corner2(tup1, tup2):
        if tup1[0] < tup2[0] and tup1[1] < tup2[1]:
            print("AC")
            return "AC"
        elif tup1[0] < tup2[0] and tup1[1] > tup2[1]:
            print("BD")
            return "BD"
        elif tup1[1] < tup2[1]:
            print("DB")
            return "DB"
        print("CA")
        return "CA"

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
