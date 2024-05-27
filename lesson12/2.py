# Создать класс BookCard, в классе должны быть:

# - private атрибут author - автор (тип str)
# - private атрибут title - название книги (тип str)
# - private атрибут year - год издания (тип int)
# - магический метод __init__, который принимает author, title, year
# - магические методы сравнения для сортировки книг по году издания
# - сеттеры и геттеры к атрибутам author, title, year. В сеттерах сделать проверку
#   на тип данных, если тип данных не подходит, то бросить ValueError. Для года
#   издания дополнительно проверить на валидность (> 0, <= текущего года).

# Аксессоры реализоваться через property.
# """

from datetime import date
CURRENT_YEAR = date.today().year

class BookCard:
   
    __year: int = 0
    author: str
    
    def __init__(self, author, year) -> None:
        self.author = author
        self.__year = year
        
    @property #getter
    def year(self):
        return self.__year
    
    @year.setter
    def year(self, val):
        if self.__check_year(val):
            self.__year = val
        else:
            raise ValueError('ValueError') 

book = BookCard('xdsdf', 200)
print(book.year)
book.year = 10
print(book.year)
book.__year = 10
print(book.year)



            
#     def __repr__(self):
#         return f" Author:{self.author},Title:{self.__title},Year:{self.__year}"

#     def __eq__(self, other) -> bool:
#         return self.__year == other.__year
#     def __lt__(self, other) -> bool:
#         return self.__year < other.__year
#     def __ne__(self, other) -> bool:
#         return self.__year != other.__year
#     def __le__(self, other) -> bool:
#         return self.__year <= other.__year
#     def __gt__(self, other) -> bool:
#         return self.__year > other.__year
#     def __ge__(self, other) -> bool:
#         return self.__year >= other.__year
    
# books = [
#     BookCard('Лев Толстой','Война и мир', 1869 ),
#     BookCard('Маргарет Мит­челл', 'Унесён­ные ветром', 1936),
#     BookCard('Олдос Хаксли', 'Дивный новый мир', 1932),
#     BookCard('Уильям Шекспир', 'Король Лир', 1603),
#     BookCard('Мар­сель Пруст', 'В поис­ках поте­рян­но­го вре­мени', 1913)
# ]