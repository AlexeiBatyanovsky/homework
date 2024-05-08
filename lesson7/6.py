str = input('Enter name and mark: ').split()
dict1 = dict()
key = str[0]
dict1[key] = str[1]
print(dict1)
while str[0] != 'stop':
    str = input('Enter name and mark: ').split()
    key = str[0]
    dict1[key] = str[1]
    print(dict1)

del dict1['stop']
