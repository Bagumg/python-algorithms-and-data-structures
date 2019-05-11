# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
# Результаты анализа вставьте в виде комментариев к коду.
# Также укажите в комментариях версию Python и разрядность вашей ОС.


import sys

def add(a, b):
    return (a + b)

	
def sub(a, b):
    return (a - b)

	
def mul(a, b):
    return (a * b)

	
def div(a, b):
    return (a / b)

	
def simple_num(n):
    lst = []
    for i in range(2, n+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            lst.append(i)
    return lst

	
print(sys.getsizeof(add(2, 2)))
print(sys.getsizeof(sub(2, 2)))
print(sys.getsizeof(mul(2, 2)))
print(sys.getsizeof(div(2, 2)))
print(sys.getsizeof(simple_num(1000)))


# 28
# 24
# 28
# 24
# 1448
# Python 3.7
# Windows 7 x64