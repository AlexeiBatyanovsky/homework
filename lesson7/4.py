a = int(input('Введите число от 3 до 20: '))

if 3 <= a <= 20:
    for i in range(a):
        if i % 2 == 0:
            print(('*' * (i + 1)).center(a))
else:
    print('Неверное значение')