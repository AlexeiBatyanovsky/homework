def rectangle(s1, s2, p):
    if p == 's':
        return s1 * s2
    elif p == 'p':
        return 2 * (s1 + s2)
    else:
        return 'error'

a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = input('Enter param s or p:')
print(rectangle(a, b, c))