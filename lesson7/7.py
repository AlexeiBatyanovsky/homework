# Запросить любое число не менее 10. 
# Вывести на экран сумму квадратов каждой цифры составляющей это число. 
# Например: дано 236 => 2*2 + 3*3 + 6*6 = 49

s = 0
num = input('Enter a number: ')
for n in num:
    s += int(n)**2
print(s)