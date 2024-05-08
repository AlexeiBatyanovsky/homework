# Запросить у учителя оценки ученика до тех пор пока он не введет 0. 
# Выдать средний бал ученика.

# вариант 1

av_mark, n = 0, 0
mark = int(input('Enter mark: '))

while mark != 0:
    n += 1
    av_mark += mark
    mark = int(input('Enter mark: '))
else:
    print('Average mark: ', av_mark/n)

# вариант 2

a = []
b = input('Enter mark: ')
while b!='0':
    b = input('Enter mark: ')
    a.append(int(b))
print(f'Average mark {sum(a)/(len(a) - 1)}')

