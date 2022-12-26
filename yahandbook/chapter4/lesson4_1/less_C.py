# Длина числа

def number_length(num):
    if num < 0:
        return len(str(num)[1:])  # delete -
    else:
        return len(str(num))

