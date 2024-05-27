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

# from datetime import date

# CURRENT_YEAR = date.today().year

from datetime import date

CURRENT_YEAR = date.today().year


class BookCard:
    __author = str
    __title = str
    __year = int

    def __init__(self, author:str, title:str, year:int) -> None:
        self.__author = author
        self.__title = title
        self.__year = year

    def __eq__(self, other) -> bool:
        return self.__year == other.__year
    def __lt__(self, other) -> bool:
        return self.__year < other.__year
    def __ne__(self, other) -> bool:
        return self.__year != other.__year
    def __le__(self, other) -> bool:
        return self.__year <= other.__year
    def __gt__(self, other) -> bool:
        return self.__year > other.__year
    def __ge__(self, other) -> bool:
        return self.__year >= other.__year
    


books = [
    BookCard('Лев Толстой','Война и мир', 1869 ),
    BookCard('Маргарет Мит­челл', 'Унесён­ные ветром', 1936),
    BookCard('Олдос Хаксли', 'Дивный новый мир', 1932),
    BookCard('Уильям Шекспир', 'Король Лир', 1603),
    BookCard('Мар­сель Пруст', 'В поис­ках поте­рян­но­го вре­мени', 1913)
]

# print(books[1].__eq__(books[2]))
# print(books[1].__lt__(books[2]))
# print(books[1].__ne__(books[2]))
# print(books[1].__le__(books[2]))
# print(books[1].__gt__(books[2]))
# print(books[1].__ge__(books[2]))
    
