# Написать функцию dict_from_args, которая принимает неограниченное
# количество позиционных аргументов и неограниченное количество аргументов
# ключевых-слов.

# Если все позиционные аргументы - целые числа, то рассчитать их сумму. Если
# нет, то кинуть ошибку TypeError("Все позиционные аргументы должны быть целыми").

# Если все именованные аргументы - ключевые слова являются строками, то найти максимальную
# длину слова. Если нет, то кинуть ошибку TypeError("Все аргументы - ключевые
# слова должны быть строками").

# Функция должна вернуть словарь, вида:
# {
#     "args_sum": 13,
#     "kwargs_max_len": 7
# }

def dict_from_args(*args, **kwargs):
    sum_args = 0
    for i in args:
        if type(i)==int:
            sum_args = sum_args+i
        else:
            raise ValueError("Все позиционные аргументы должны быть целыми")
    
    kwargs_max_len = 0
    for n in kwargs:
        if type(kwargs.keys)==str:
           kwargs_max_len = len(n)
        else:
            raise ValueError("Все аргументы - ключевые слова должны быть строками")
            
           
    return {'args_sum':sum_args, 'kwargs_max_len':kwargs_max_len}
  
        
print(dict_from_args(5, 6, 12, 45, 6, 9, word='jfnfjk', word1='jnjk', word2='jjkh', word3='jjk'))
