# Модернизация системы вывода
data = set()
def modern_print(string):
    global data
    data.add(string)
    return data   
        


print(modern_print("Hello"))
print(modern_print("Hello World"))
print(modern_print("Hello"))
print(modern_print("Hello World Keys"))

print(data)


