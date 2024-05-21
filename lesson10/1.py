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
        if isinstance(i, int):
            sum_args = sum_args+i
        else:
            raise ValueError("Все позиционные аргументы должны быть целыми")
    
    kwargs_max_len = 0
    for key, val in kwargs.items():
        if isinstance(val, str):
            for n in range(len(val)):
                kwargs_max_len += 1
                
        else:
            raise ValueError("Все аргументы - ключевые слова должны быть строками")
            
        return {'args_sum':sum_args, 'kwargs_max_len':kwargs_max_len},
        
print(dict_from_args(5, 6, 12, 45, 6, 9, word0='jfdjjfjk', word1='jchjjhbghh', word2='jjkchjhbjhbghh', word3='jjk'))
