# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции.
# По возможности доработайте алгоритм (сделайте его умнее).


import random

arr = [random.randint(-100, 100) for i in range(20)]

def bubble_sort(arr):
    for j in range(len(arr)):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr

def bubble_sort_upgraded(arr):
    is_sorted = False
    for j in range(len(arr)):
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr

print(arr)
print(bubble_sort(arr))
print(bubble_sort_upgraded(arr))

# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

arr = [random.randint(0, 50) for i in range(20)]


def div_array(arr):
    if len(arr) <= 1:
        return arr
    middle = int(len(arr) / 2)
    left = div_array(arr[:middle])
    right = div_array(arr[middle:])
    return merge_arr(left, right)


def merge_arr(left, right):
    merged_arr = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            merged_arr.append(left[0])
            left = left[1:]
        else:
            merged_arr.append(right[0])
            right = right[1:]
    if len(left) > 0:
        merged_arr += left
    if len(right) > 0:
        merged_arr += right
    return merged_arr

print(div_array(arr))

# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
# Задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
# то используйте метод сортировки, который не рассматривался на уроках


m = int(input('Введите длину массива: ' ))
arr = [random.randint(0, 100) for i in range(2 * m + 1)]

def median(arr):
    left = 0
    right = len(arr) - 1

    while left <= right:
        for i in range(left, right, +1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        right -= 1

        for i in range(right, left, -1):
            if arr[i - 1] > arr[i]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
        left += 1
    return arr

print(arr)
print(median(arr))
mediana = median(arr)
print('Медиана равна: ' + str(mediana[m]))