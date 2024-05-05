def factorial(n):
    if n == 0:
        return 1
    return factorial(n - 1) * n

x = int(input('Enter number: '))
print(factorial(x)) 