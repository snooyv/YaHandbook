# Генератор матриц

# size = tuple
def make_matrix(size, value=0):
    if len(size) == 1:
        x, = size
        y = x
    else:
        x, y = size
    return [[value] * x for i in range(y)]


print(make_matrix((3, 4), 4))
