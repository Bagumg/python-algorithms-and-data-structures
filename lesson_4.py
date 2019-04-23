import timeit
import cProfile

# 1. Проанализировать скорость и сложность одного любого алгоритма,
# разработанных в рамках домашнего задания первых трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.


def add(a, b):
    return (a + b)

def sub(a, b):
    return (a - b)

def mul(a, b):
    return (a * b)

def div(a, b):
    return (a / b)

print(timeit.timeit('add(1, 2)', setup='from __main__ import add', number=100))
print(timeit.timeit('sub(1, 2)', setup='from __main__ import sub', number=100))
print(timeit.timeit('mul(1, 2)', setup='from __main__ import mul', number=100))
print(timeit.timeit('div(1, 2)', setup='from __main__ import div', number=100))


# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»
# Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов. Результаты анализа сохранить в виде комментариев в файле с кодом.


def simple_num(n):
    lst = []
    for i in range(2, n+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            lst.append(i)
    return lst


n = int(input("Введите число n: "))
print(simple_num(n))
print(timeit.timeit('simple_num(1000)', setup='from __main__ import simple_num', number=100))


# Решето Эратосфена


def sieve(n):
    a = list(range(n+1))
    a[1] = 0
    for i in a:
        if i > 1:
            for j in range(i + i, len(a), i):
                a[j] = 0
    return [x for x in a if x != 0]

n = int(input("Введите число n: "))
print(sieve(n))
print(timeit.timeit('sieve(100000)', setup='from __main__ import sieve', number=100))
