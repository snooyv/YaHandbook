# Простая задача (простое число)

def is_prime(num):
    if num == 2:
        return True
    i = 3
    while i * i <= num and num % i != 0:
        i += 2
    return i * i > num

print(is_prime(18))