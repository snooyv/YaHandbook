# Rectangle2

import math


class Rectangle:
    def __init__(self, tup1, tup2):
        self.x1, self.y1 = tup1
        self.x2, self.y2 = tup2
        self.flag = False

        if self.check_corner(tup1, tup2) == "DB":
            self.flag = True

    def get_pos(self):
        if self.flag:
            return round(self.x2, 2), round(self.y2, 2)
        return round(self.x1, 2), round(self.y2, 2)

    def get_size(self):
        ab = self.light(self.x1, self.y1, self.x1, self.y2)
        bc = self.light(self.x1, self.y2, self.x2, self.y2)
        return round(bc, 2), round(ab, 2)

    def move(self, dx, dy):
        self.x1 += dx
        self.y1 += dy
        self.x2 += dx
        self.y2 += dy

    #def resize():

    @staticmethod
    def check_corner(tup1, tup2):
        if tup1[0] < tup2[0] and tup1[1] < tup2[1]:
            print("AC")
            return "AC"
        print("DB")
        return "DB"

    @staticmethod
    def light(p1x, p1y, p2x, p2y):
        dx = p1x - p2x
        dy = p1y - p2y
        return math.hypot(dx, dy)
