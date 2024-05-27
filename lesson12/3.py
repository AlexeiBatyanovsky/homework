# в файле hero1 добавить следующий функционал
#         - добавить несколько классов других героев унаследовав их от Hero.
#         - Каждому герою добавить уникальное свойство-спец.очки (мана, ярость, и т.п. ) и 
#                 и свойство отражающее урон от спец.атаки.
#         - Создать метод атаки special_attack которая возможна только если количество 
#                 спец.очков более 0.
#         - Добавить метод atack который при атаке с вероятностью 25% будет использовать 
#                 спец.способность героя если у него остались спец.очки. 
#                 При спец атаке вычитать из очков 1. Если вероятность пришлась на
#                 остальные 75% - выполнить обычную атаку. Вывести сообщение в консоль 
#                 о типе и результате атаки.

# добавить класс Arena:
#         - атрибут warriors - все воины на арене (тип list)
#         - магический метод __init__, который принимает необязательный аргумент warriors.
#                 Если был передан список warriors, та заполняет им атрибут. Если нет, то заполняет
#                 пустым списком.
#         - метод add_warrior, который принимает аргумент warrior и добавляет его к warriors.
#                 Если данный воин уже есть в списке, то бросить исключение ValueError("Воин уже на арене").
#                 Если нет, то добавить воина к списку warriors и вывести сообщение на экран
#                 "{warrior.name} участвует в битве"
#         - метод choose_warrior, который не принимает аргументов и возвращает случайного
#                 воина из warriors
#         - метод battle, который не принимает аргументов и симулирует битву. Сперва 
#                 должна пройти проверка, что воинов на арене больше 1. Если меньше, то бросить
#                 исключение ValueError("Количество воинов на арене должно быть больше 1").
#                 Битва продолжается, пока на арене не останется только один воин. Сперва
#                 в случайном порядке выбираются атакующий и защищающийся. Атакующий ударяет
#                 защищающегося. Если у защищающегося осталось 0 health_points, то удалить его
#                 из списка воинов и вывести на экран сообщение "{defender.name} пал в битве".
#                 Когда останется только один воин, то вывести сообщение "Победил воин: {winner.name}".
#                 Вернуть данного воина из метода battle.
                
                
# Создать несколько воинов используя разные классы, добавить их на арену и запустить битву. 
# Выжить должен только один.

class Hero:
    """     
    Класс для создания героя 
    
     ...

    Attributes
    ----------
    name : str
        Имя героя
    health : int
        здоровье героя 
    age : int
        age of the person

    Methods
    -------
    print_info():
        Печатает в консоль информацию о герое
    
    kick():
        производит один удар - высчитывает и уменьшает броню и здоровье 
    
    """

    def __init__(self, name, health, armor, strong) -> None:
        self.name = name
        self.health = health
        self.armor = armor
        self.strong = strong
    
    def _get_info(self):
        print(
              f"Имя {self.name}\n" \
              f"Здоровье - {self.health}\n" \
              f"Защита {self.armor}"
        )
        
    def print_info(self):
        
        print(self._get_info() + '\n')
    
    
    def special_attack(self, points):
        if points > 0:

    def attack(self, other):
        other.armor -= self.strong
        if other.armor < 0:
            other.health += other.armor
            other.armor = 0



class Mage(Hero):
    def __init__(self, name, health, armor, strong, mana, manashield) -> None:
        super().__init__(name, health, armor, strong)
        self.mana = mana
        self.manashield = manashield
class Rogue(Hero):
    def __init__(self, name, health, armor, strong, energy, evasion) -> None:
        super().__init__(name, health, armor, strong)
        self.energy = energy
        self.evasion = evasion

class Warrior(Hero):
    def __init__(self, name, health, armor, strong, rage, blocking) -> None:
        super().__init__(name, health, armor, strong)
        self.rage = rage
        self.blocking = blocking
