# Создать класс Student.

# Определить атрибуты:
#     - surname - фамилия
#     - name - имя
#     - group - номер группы
#     - grads - список оценок

# Определить методы:
#     - инициализатор __init__
#     - Методы __eq__, __ne__, __lt__, __gt__, __le__, __ge__, которые будут сравнивать
#     студентов по среднему баллу
#     - метод add_grade - добавляет в список оценок одну или несколько оценок от 1 до 10
#     - метод average_grade -считает и возвращает среднюю оценку ученика

# Создать список из 5 студентов класса и вывести его отсортированным по возрастанию
# и убыванию.

# Вывести студентов, у которых средний балл больше 8


class Student:
    def __init__(self,surname, name, group, grads:list) -> None:
        self.surname = surname
        self.name = name
        self.group = group
        self.grads = grads
    
    # def __str__(self) -> str:
    #     return f"surname:{self.surname}\nname:{self.name}\ngroup:{self.group}\ngrads:{self.grads}"
    
    def add_grade(self, arg:int):
        self.grads.append(arg)
        return(self.grads)

    def average_grade(self):
        return sum(self.grads) / len(self.grads)
    
student1 = Student('Pupkin','Vasia', 'a', [8, 10, 7, 9, 10, 6])
student2 = Student('lupkin','Petya', 'b', [8, 10, 10, 9, 10, 8])
student3 = Student('Pushkin','Ivan', 'c', [8, 7, 7, 9, 7, 6])
student4 = Student('Supkin','Anton', 'b', [8, 6, 7, 9, 6, 6])
student5 = Student('Pukin','Dima', 'a', [8, 5, 7, 6, 4, 6])

#print(student1.__str__())
print(student2.average_grade())
print(student3.add_grade(6))