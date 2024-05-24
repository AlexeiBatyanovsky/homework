# Описать абстрактный класс Animal у которого:

# - атрибут name - кличка (тип str)
# - магический метод __init__, который принимает аргумент name
# - абстрактный метод says, который не принимает аргументов

# На основе Animal определить классы Cat, Dog, Cow, которые переопределят метод
# says таким образом, чтобы он возвращал строку вида:

# - "{кличка} - кошка. Говорит МЯУ!" для класса Cat
# - "{кличка} - собака. Говорит ГАВ!" для класса Dog
# - "{кличка} - корова. Говорит МУ!" для класса Cow

from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self,name) -> None:
        self.name = name

    @abstractmethod
    def says(self):
        pass

class Cat(Animal):

    def __init__(self, name) -> None:
        super().__init__(name)

    def says(self):

        return f'{self.name} - кошка. Говорит МЯУ!'
    
class Dog(Animal):

    def __init__(self, name) -> None:
        super().__init__(name)

    def says(self):

        return f'{self.name} - собака. Говорит ГАВ!'
    
class Cow(Animal):

    def __init__(self, name) -> None:
        super().__init__(name)

    def says(self):

        return f'{self.name} - корова. Говорит МУ!'


animal_1 = Cat('Мурка')
animal_2 = Dog('Шарик')
animal_3 = Cow('Зорька')

print(animal_1.says())
print(animal_2.says())
print(animal_3.says())