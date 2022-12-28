# Функциональный НОД
from functools import reduce


def gcd(*args):
    if len(args) == 1:
        return args[0]
    result = reduce(gcd_two_number, args)

    return result

def gcd_lambda(*args):
    if len(args) == 1:
        return args[0]
    tmp = args[0]
    i = 1
    for i in args:
        tmp = gcd_two_number(tmp, i)
    return tmp


def gcd_two_number(num1, num2):
    while num1 != num2:
        if num1 > num2:
            num1 -= num2
        else:
            num2 -= num1
    return num1


print(gcd(36, 48, 156, 100500))
print(gcd_lambda(36, 48, 156, 100500))
# result = reduce(gcd_two_number, [3, 6, 12])
# print(result)
