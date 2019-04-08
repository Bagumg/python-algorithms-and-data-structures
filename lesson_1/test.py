digit_one = [int(x) for x in input('Введите первое число: ')]
digit_two = [int(x) for x in input('Введите второе число: ')]
if sum(digit_one) > sum(digit_two):
    print(''.join(map(str, digit_one)))
    print(sum(digit_one))
else:
    print(''.join(map(str, digit_two)))
    print(sum(digit_two))