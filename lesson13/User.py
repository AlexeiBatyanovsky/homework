# Создать класс User с атрибутами:

# Свойства:
# 	- name - имя - содержит только буквы русского алфавита 
# 	- login - логин - может содержать  только латинские буквы цифры и черту подчеркивания быть не менее 6 символов
# 	- password - пароль - может содержать  только латинские буквы цифры. Обязательные условия: 
#                 содержит менее шести символов
#                 содержит строчную букву
#                 содержит заглавную букву
#                 содержит число
# 	- is_blocked - заблокирован
# 	- subscription_date - дата до какой действует подписка
# 	- subscription_mode - вид подписки (free, paid)


# Методы:
# 	- bloc - принимает логическое значение и помечает пользователя заблокированным 
# 	- check_subscr - может принимать аргумент в виде даты. Проверяет действует ли подписка на определенную дату. 
# 						Если дата не передана значит на дату проверки. 
# 						Возвращает  действует ли подписка, ее вид и сколько осталось дней.
# 	- change_pass - смена пароля и присваивание его в качестве действующего. 
# 						Пароль должен пройти валидацию. 
# 						Если пароль не был передан сгенерировать по правилам и вывести в консоль.
# 	- get_info - выводит информацию о пользователе если заблокирован то сообщает об этом.



# Создание объекта должно происходить  при передаче обязательных аргументов имя и логин и необязательного - пароль. Логин и пароль должны быть проверен на валидность.
# Если пароль в конструктор не был передан он должен сгенерироваться на основании правил, и должен быть выведен на экран(консоль).
# При создании пользователя ему предоставляется пробная подписка сроком на 30 дней.
# При изменении даты подписки  вид подписки меняется на платный.
# Валидацию данных сделать через регулярные выражения

import re
import random
from datetime import date, timedelta

class User():

    def __init__(self, name:str, login:str, password = None) -> None:
        self.name = name
        self.login = login
        self.password = password
        self.is_blocked = False
        self.subscription_mode = 'free'
        self.subscription_date = date.today() + timedelta(days=30)

    def __str__(self) -> str:
        return f'name:{self.name}, login:{self.login}, password:{self.password}'
                   
    def get_info(self):
        print(f'name:{self.name}, login:{self.login}, password:{self.password}, blocked:{self.is_blocked},'\
               f' subscription_mode:{self.subscription_mode}, subscription_date:{self.subscription_date}')
        
    def bloc(self, is_blocked):
        self.is_blocked = is_blocked
        
    def change_pass(self, password = None):
        if password:
            password = gen_pass()
        else:
            self.password = password

    def check_subscr(self, date_sub = None):
        date_sub = date_sub if date_sub else date.today()
        if date_sub <= self.subscription_date:
            days = (self.subscription_date - date_sub).days
            return f"Подписка: {self.subscription_mode} активна {days} дней"
        else:
            return f"Подписка закончилась"
            
    def __checkname(self, name):
        return re.match(r'^[а-яА-ЯёЁ]{1,}$', name)
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, val):
        if self.__checkname(val):
            self.__name = val
        else:
            raise ValueError('Используйте только буквы русского алфавита')
        
    def __checklogin(self, login):
        return re.match(r'^[a-zA-Z0-9_]{6,}$', login)
    
    @property
    def login(self):
        return self.__login
    
    @login.setter
    def login(self, val):
        if self.__checklogin(val):
            self.__login = val
        else:
            raise ValueError('Используйте только латинские буквы, цифры и черту подчеркивания, не менее 6 символов')
    
    def __checkpassword(self, password):
        return re.match(r'^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z]{6,}$', password)
    
    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, val):
        if val == None:
            self.__password = gen_pass(val)
        else:
            if self.__checkpassword(val):
                self.__password = val
            else:
                raise ValueError('Используйте только латинские буквы, цифры, не более 6 символов')
    
def gen_pass(password):

        chars1 = 'abcdefghijklnopqrstuvwxyz'
        chars2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        chars3 = '1234567890'
        length = int(random.uniform(2, 6))
        password =''
        for i in range(length):
            password += random.choice(chars1)
            password += random.choice(chars2)
            password += random.choice(chars3)
        return password  
       
user1 = User('Василий','Vasilii', 'AhRgnlg8')
user2 = User('Анатолий', 'Anatolii')
user3 = User('Александр', 'Aleksandr')

user1.get_info()
user1.bloc(True)
user1.get_info()
user1.change_pass()
user1.get_info()
print(user1.check_subscr())
   
