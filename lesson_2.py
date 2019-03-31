# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем.
# После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные для вычислений.
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то
# программа должна сообщать ему об ошибке и снова запрашивать знак операции.
# Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.


# До просмотра урока

print('Программа складывает, вычитает, умножает или делить два числа')
print('Для выхода, вместо операции введите 0')

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = input('Введите операцию:')
while c != '0':
    if c == '+':
        print(a + b)
    elif c == '-':
        print(a + b)
    elif c == '*':
        print(a * b)
    elif c == '/':
        if b == 0:
            print('На ноль делить нельзя!')
        else:
            print(a / b)
    else:
        print('Введите правильный знак операции')
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    c = input('Введите операцию:')


# После просмотра урока

def add(a, b):
    return (a + b)

def sub(a, b):
    return (a - b)

def mul(a, b):
    return (a * b)

def div(a, b):
    return (a / b)

def menu():
    print('Выберите действие:')
    answer = input('1 - сложение\n2 - вычитание\n3 - умножение\n4 - деление.\nВведите - 0 для выхода\n')
    first_num = int(input('Введите первое число: '))
    second_num = int(input('Введите второе число: '))
    print(commands[answer](first_num, second_num))

commands = {
    '1': add,
    '2': sub,
    '3': mul,
    '4': div
}
answer = ''
while answer != '0':
    menu()


# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

x = input('Введите натуральное число: ')
even = []
odd = []
for i in x:
    if int(i) % 2 == 0:
        even.append(int(i))
    elif int(i) % 2 != 0:
        odd.append(int(i))
print(even)
print(odd)

# Ещё вариант

x = input('Введите натуральное число: ')
even = []
list(even.append(i) for i in x if int(i) % 2 == 0)
odd = []
list(odd.append(i) for i in x if int(i) % 2 != 0)
print(even)
print(odd)


# 3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, то надо вывести число 6843.

x = input('Введите число: ')
print(x[::-1])


# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

n = int(input('Введите количество элементов: '))
digits = []
counter = 1
for i in range(n):
    counter = counter / 2
    digits.append(counter)
print(sum(digits))


# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

for i in range(32, 128):
    print(chr(i), end=' ')
    if (i - 1) % 10 == 0:
        print()


# 6. В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число,
# чем то, что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.

# Мы же делали это задание на прошлом уроке.

from random import randint

guessesTaken = 0
n = int(input('Введите верхнее число диапазона:'))
k = int(input('Сколько попыток желаете использовать?:'))

number = randint(1, n)

while guessesTaken <= k:
    print('Угадайте, какое число я загадал')
    guess = input()
    guess = int(guess)
    guessesTaken = guessesTaken + 1
    if guess < number:
        print('Загаданное число больше')
    elif guess > number:
        print('Загаданное число меньше')
    elif guess == number:
        print('Вы угадали')
    if guessesTaken == k:
        print('Попытки закончились')


# 7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n - любое натуральное число.

n = int(input('Введите натуральное число: '))
counter = 1
sum = 0
for i in range(n):
    sum = sum + counter
    counter += 1
if sum == (n * (n + 1)) / 2:
    print('Равенство верно')
else:
    print('Равенство не верно')


# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

n = input('Введите последовательность чисел: ')
x = int(input('Введите число, которое необходимо посчитать: '))
counter = 0
for i in n:
    if int(i) == x:
        counter += 1
print(f'Число {x} встречается {counter} раз')


# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

digit_one = [int(x) for x in input('Введите первое число: ')]
digit_two = [int(x) for x in input('Введите второе число: ')]
if sum(digit_one) > sum(digit_two):
    print(''.join(map(str, digit_one)))
    print(sum(digit_one))
else:
    print(''.join(map(str, digit_two)))
    print(sum(digit_two))