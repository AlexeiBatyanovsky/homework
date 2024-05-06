r = ""
str = input('Enter string: ')

for i in range(1, len(str) + 1):
    r += str[i - 1] * i
    
print(r)