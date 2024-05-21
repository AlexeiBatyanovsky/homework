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

def dict_from_args(*args:int, **kwargs:str):

    # sum_args = 0
    # for arg in args:
    #     if isinstance(arg, int):
    #         sum_args = sum_args+arg
    #     else:
    #         raise ValueError("Все позиционные аргументы должны быть целыми")
   
    # kwargs_max_len = 0
    # for kwarg in kwargs.values():
    #     if isinstance(kwarg, str):
    #         kwargs_max_len = len(max(list(kwargs.values()), key=len))
    #     else:
    #         raise ValueError("Все аргументы - ключевые слова должны быть строками")
            
    #     return{'args_sum':sum_args, 'kwargs_max_len':kwargs_max_len}

    if not all(map(lambda arg: isinstance(arg, int), args)):
        raise ValueError("Все позиционные аргументы должны быть целыми")
    
    if not all(map(lambda kwarg: isinstance(kwarg, str), kwargs.values())):
        raise ValueError("Все аргументы - ключевые слова должны быть строками")
    sum_args = sum(args)
    kwargs_max_len = len(max(kwargs.values()))
    return{'args_sum':sum_args, 'kwargs_max_len':kwargs_max_len}
        
print(dict_from_args(5, 6, 12, 45, 6, 9, word0='jfdjfjk', word1='jchjjhbghh', word2='jjkchjbjhbghh', word3='jjk'))
