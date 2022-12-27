# Шахматный обед

def can_eat(tuple1, tuple2):
    x1, y1 = tuple1
    x2, y2 = tuple2

    if (abs(x1 - x2) * abs(y1 - y2)) == 2:
        return True

    return False
        

print(can_eat((2, 1), (4, 2)))
print(can_eat((5, 5), (6, 6)))

