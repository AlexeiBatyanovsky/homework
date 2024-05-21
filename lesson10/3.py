# Написать функцию hello, которая принимает аргумент name - строку с именем и
# выводит принтом "Привет, {name}"

# Написать декоратор log_decorator, который перед выполнением
# функции печатает на экран строку, вида
# Выполняеся функция <имя> с аргусентами <аргументы> 
# После выполнения функции напечатать строку "<имя функции> - завершена"

def log_decorator(func):
    def accepting_arg(arg):
        print(f"Выполняется функция {func.__name__} с аргументами {arg}")
        func(arg)
        print(f"{func.__name__} - завершена")
    return accepting_arg

@log_decorator
def hello(name):
    print(f'Hello, {name}')
print(hello('Vasia'))