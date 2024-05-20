def my_shiny_new_decorator(function_to_decorate):
     # Внутри себя декоратор определяет функцию-"обёртку". Она будет обёрнута вокруг декорируемой,
     # получая возможность исполнять произвольный код до и после неё.
     def the_wrapper_around_the_original_function():
         print("Я - код, который отработает до вызова функции")
         function_to_decorate() # Сама функция
         print("А я - код, срабатывающий после")
     # Вернём эту функцию
     return the_wrapper_around_the_original_function

@my_shiny_new_decorator
def beef(food="### говядина ###"):
    print(food)
print(beef())