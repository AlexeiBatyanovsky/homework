# Создать класс Phone, у которого будут следующие атрибуты:

# Определить атрибуты:

# - brand - бренд
# - model - модель
# - issue_year - год выпуска

# Определить методы:

# - инициализатор __init__
# - receive_call, который принимает имя звонящего и выводит на экран: 
#         <Бренд-Модель> - Звонит {name}
# - get_info, который будет возвращать кортеж (brand, model, issue_year)
# - метод __str__, который выводит на экран информацию об устройстве:
# Бренд: {}
# Модель: {}
# Год выпуска: {}


class Phone:
    def __init__(self, brand:str, model:str, issue_year:int) -> None:
        self.brand = brand
        self.model = model
        self.issue_year = issue_year

    def receive_call(self, name:str) -> str:
        return f'{self.brand}-{self.model} - Звонит {name}'

    def get_info(self) -> tuple:
        return (self.brand, self.model, self.issue_year)
        

    def __str__(self) -> str:
        return f" Brand:{self.brand}\n model:{self.model}\n issue_year:{self.issue_year}"

phone1 = Phone('Samsung', 's24',2024)
phone2 = Phone('Apple', 'iphone 15',2023)
phone3 = Phone('Xiaomi', '14',2024)

print(phone3.receive_call('Petia'))
print(phone2.get_info())
print(phone1)

