str1 = input('Enter string: ')
def money(n):
    n = str1[::-1]
    return(print(' '.join(n[i:i+3] for i in range(0, len(n), 3))[::-1],'руб.'))

print(money(str1))