import math


class Rectangle:

    def __init__(self, tuple1, tuple2, bx=0, by=0):
        flag = self.chek_corner2(tuple1, tuple2)
        if flag == "AC":
            self.x1, self.y1 = tuple1
            self.x2, self.y2 = tuple2
            self.bx = self.x1
            self.by = self.y2
        elif flag == "DB":
            self.bx, self.by = tuple2
            self.x1 = self.bx
            self.y1 = tuple1[1]
            self.x2 = tuple1[0]
            self.y2 = self.by

    #def set_corner(self, flag,  tuple1, tuple2):

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
        ab = self.light(self.x1, self.y1, self.bx, self.by)
        bc = self.light(self.bx, self.by, self.x2, self.y2)
        return f"{2 * (ab + bc):.2f}"

    @staticmethod
    def light(p1x, p1y, p2x, p2y):
        dx = p1x - p2x
        dy = p1y - p2y
        return math.hypot(dx, dy)

    def area(self):
        ab = self.light(self.x1, self.y1, self.x1, self.y2)
        bc = self.light(self.x1, self.y2, self.x2, self.y2)
        return f"{ab * bc:.2f}"

    def get_pos(self):
        return round(self.bx, 2), round(self.by, 2)

    def get_size(self):
        ab = self.light(self.x1, self.y1, self.x1, self.y2)
        bc = self.light(self.x1, self.y2, self.x2, self.y2)
        return round(bc, 2), round(ab, 2)

    def move(self, dx, dy):
        self.x1 += dx
        self.y1 += dy
        self.x2 += dx
        self.y2 += dy

    def resize(self, width, height):
        self.x1 -= height
        self.y2 -= width
