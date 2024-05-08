# Дан списк:
# ['qwertyu','asdfggh','zxcvbnm','yuiop[]','hjklasd','mnbvnbv']
# Для каждого элемента в списке 
#     - вывести на экран сначала номер элемента 
#     - сам элемент 
#     - символ данного элемента, соответствующий номеру его позиции в списке. 
# Образец:
# 1 - qwertyu - q
# 2 - asdfggh - s
# 3 - zxcvbnm - c
# и так далее...

# вариант 1

list1 = ['qwertyu','asdfggh','zxcvbnm','yuiop[]','hjklasd','mnbvnbv']

for i in range(len(list1)):
    print(i + 1, '-', list1[i], '-', list1[i][i] )

# вариант 2

list1 = ['qwertyu','asdfggh','zxcvbnm','yuiop[]','hjklasd','mnbvnbv']

for k, i in enumerate(list1):
    print(f'{k + 1} - {i} - {i[k]}')