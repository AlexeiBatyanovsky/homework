# Написать рекурсивную функцию, которая вычисляет  
# факториал переданного в нее числа.

x = int(input('Enter number: '))

def factorial(n):
    if n == 0:
        return 1
    return factorial(n -1) * n
print(factorial(x))
