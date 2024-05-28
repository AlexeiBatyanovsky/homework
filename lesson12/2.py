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
   
    __year: int
    __author: str 
    __title: str
        
    def __check_year(self, year):
        return isinstance(year, int) and 0 < year <= CURRENT_YEAR
    
    def __check_author(self, author):
        return not isinstance(author, str)
    
    def __check_title(self, title):
        return not isinstance(title, str)
    
    def __init__(self, author,title, year) -> None:
        
        if self.__check_author(author):
            raise ValueError('Enter correct author')
        self.__author = author
        if self.__check_title(title):
            raise ValueError('Enter correct title')
        self.__title = title
        if not self.__check_year(year):
            raise ValueError('Enter correct date')
        self.__year = year
        
    @property
    def year(self):
        return self.__year
    
    @year.setter
    def year(self, val1):
        if self.__check_year(val1):
            self.__year = val1
        else:
            raise ValueError
    @property
    def author(self):
        return self.__author
    
    @author.setter
    def author(self, val2):
        if self.__check_author(val2):
            self.__year = val2
        else:
            raise ValueError
    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, val3):
        if self.__check_title(val3):
            self.__year = val3
        else:
            raise ValueError

    def __repr__(self):
        return f" Author:{self.author}\n Title:{self.__title}\n Year:{self.__year}\n"

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
    
# books = [
#     BookCard('Лев Толстой','Война и мир', 1869 ),
#     BookCard('Маргарет Мит­челл', 'Унесён­ные ветром', 1936),
#     BookCard('Олдос Хаксли', 'Дивный новый мир', 1932),
#     BookCard('Уильям Шекспир', 'Король Лир', 1603),
#     BookCard('Мар­сель Пруст', 'В поис­ках поте­рян­но­го вре­мени', 1913)
# ]

book = BookCard('Лев Толстой', 'Война и мир', 1869)