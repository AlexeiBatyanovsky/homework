def funct(a, b):
    if b:
        print(f'- {a[0]} {a[1][0]}.{a[2][0]}.')
    else:
        print(f"- {a[1][0]}.{a[2][0]}.{a[0]}")
    
fio = input('Enter FIO: ').split()
param = int(input('Enter param: '))

print(funct(fio, param))