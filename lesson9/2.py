# Написать рекурсивную функцию, которая принимает 2 аргумента 
# (целые числа - a и b) и высчитывает суммы всех чисел от a до b (включительно). 
# Пример: a = 3, b = 5 -> 12 (3+4+5)
# Пример: a = 5, b = 9 -> 35 (5+6+7+8+9)

a = int(input('enter a: '))
b = int(input('enter b: '))
list1 = list(range(a, b))

def sumList(x):
    if x==[]:
        return 0
    else:
        return x[0]+sumList(x[1:])
 
print(sumList(list1))
