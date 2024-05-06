def fio(a, b = True):
    if b:
        print(f'- {a[0]} {a[1][0]}.{a[2][0]}.')
    else:
        print(f"- {a[1][0]}.{a[2][0]}.{a[0]}")
    
a = input('Enter fio: ').split()
b = int(input('Enter param: '))

print(fio(a, b))