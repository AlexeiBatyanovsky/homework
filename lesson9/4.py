# Дан список [1,2,3,4,5,6,7,8,9]. Создать 3 копии этого списка 
# и с каждой выполнить след действия:
#     - возвести каждый элемент во 2ю степень
#     - прибавить 3 к каждому элементу значение которого является четным 
#     - элементы значения которого является 
#             четными - умножить на 2 
#             нечетным - умножить на 3

# Использовать map и lambda.

list1 = [1,2,3,4,5,6,7,8,9]

sq_num = list(map(lambda x: x * x, list1))
print(sq_num)


