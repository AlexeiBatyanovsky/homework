sr_bal = 0
bal = int
sum = 0
n = 0

while bal != 0:
    n = n + 1
    bal = int(input('Введите оценку: '))
    sum = sum + bal
    sr_bal = sum/(n)
    print(n, bal, sr_bal, sum)
else:
    print('средний балл: ', sr_bal)