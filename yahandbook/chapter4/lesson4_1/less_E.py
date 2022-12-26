# Числовая строка

def split_numbers(num_str):
    data = [int(x) for x in num_str.split()]
    return tuple(data)

result = split_numbers("1 -2 3 -4 5")
print(result)
