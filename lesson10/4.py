# Написать декоратор который позволит не останавливать программу 
# в случае если любая декорируемая функция выбрасывает ошибку, 
# а выводить имя функции в которой произошла ошибка и информацию об ошибке в консоль. 
# Имя функции можно узнать использовав свойство __name__ ( print(func.__name__) )

def error_decor(func):
    def wrapper(*args, **kwargs):
        try:
            return(func(*args, **kwargs))
        except Exception as x:
            print(f'В функции {func.__name__} произошла ошибка {x}')
    return wrapper

@error_decor
def f1(a):
    print(1/a)

f1(1)
f1(2)
f1(0)
f1(5)