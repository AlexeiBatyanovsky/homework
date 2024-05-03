a = int(input('Enter a number from 3 to 20: '))

if 3 <= a <= 20:
    for i in range(2*a):
        if i % 2 == 0:
            print(('*' * (i + 1)).center(2*a))
else:
    print('Error')