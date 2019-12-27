# 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
# (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль
# (за год для всех предприятий) и вывести наименования предприятий,
# чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.


data = dict()
firm_count = int(input('Input firms amount: '))
for i in range(firm_count):
    data[input('Input firm name: ')] = [int(input('First quarter income: ')), int(input('Second quarter income: ')),
                                        int(input('Third quarter income: ')), int(input('Fourth quarter income: '))]

print(data)
annual_income = (list(sum(v) for v in data.values()))
print(annual_income)
mid_annual_income = (int(sum(list(sum(v) for v in data.values())) / firm_count))
print(mid_annual_income)

hi = []
lo = []
for k, v in data.items():
    if sum(v) <= mid_annual_income:
        lo.append(k)
    elif sum(v) > mid_annual_income:
        hi.append(k)

print('Firms whose annual income is higher than middle income ', hi)
print('Firms whose annual income is lower than middle income ', lo)


# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

a = list(input('Введите первое число в шеснадцатиричном формате: '))
b = list(input('Введите второе число в шеснадцатиричном формате: '))

print(int(''.join(a), 16) + int(''.join(b), 16))
print(int(''.join(a), 16) * int(''.join(b), 16))
