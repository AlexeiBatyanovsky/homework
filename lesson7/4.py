# Запросить высоту елочки - число от 3 до 20. 
# Напечатать на экране елочку где ее высото равна числу строк. 
# Пример елочки из 4 строк:
#    *
#   ***
#  *****
# *******

# вариант 1

a = int(input('Enter a number from 3 to 20: '))

if 3 <= a <= 20:
    for i in range(2*a):
        if i % 2 == 0:
            print(('*' * (i + 1)).center(2*a))
else:
    print('Error')

# вариант 2

SPACE = ' '
STARS = '*'

rows = int(input("Enter a number from 3 to 20: "))
spaces = rows -1
stars = 1

for i in range(rows):
    print(
        (SPACE * spaces) +
        (STARS * stars) +
        (SPACE * spaces)
    )
    stars += 2
    spaces -=1