list1 = list(map(int, input(('Enter a number: '))))
sum = 0
for i in range(len(list1)):
    square = list1[i] ** 2
    sum = sum + square
    #print(square)
    #print(sum)
print(sum)