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
    def __init__(self,surname:str, name:str, group:str, grads:list) -> None:
        self.surname = surname
        self.name = name
        self.group = group
        self.grads = grads
       
    def __repr__(self):
        return f"surname:{self.surname}, name:{self.name}, group:{self.group}, grads:{self.grads}\n"
    
    # def __str__(self) -> str:
    #     return f"surname:{self.surname}, name:{self.name}, group:{self.group}, grads:{self.grads}"

    def __eq__(self, other) -> bool:
        return self.average_grade() == other.average_grade()
    def __lt__(self, other) -> bool:
        return self.average_grade() < other.average_grade()
    def __ne__(self, other) -> bool:
        return self.average_grade() != other.average_grade()
    def __le__(self, other) -> bool:
        return self.average_grade() <= other.average_grade()
    def __gt__(self, other) -> bool:
        return self.average_grade() > other.average_grade()
    def __ge__(self, other) -> bool:
        return self.average_grade() >= other.average_grade()
       
    def add_grade(self, arg:int):  
        if 0 <= arg <= 10:
            self.grads.append(arg)
        else:
            raise ValueError("input 0 <= arg <= 10")
        return(self.grads)

    def average_grade(self):
        return sum(self.grads) / len(self.grads)

students =[
    Student('Pupkin','Vasia', '№1', [8, 10, 9, 9, 10, 6]),
    Student('Krupkin','Petya', '№2', [10, 10, 9, 9, 10, 8]),
    Student('Lunkin','Ivan', '№3', [8, 7, 7, 9, 7, 6]),
    Student('Turkin','Anton', '№2', [8, 8, 7, 9, 8, 10]),
    Student('Bulkin','Dima', '№1', [8, 5, 7, 6, 4, 6])
]

# print(students[1]==(students[2]))
# print(students[1]!=(students[2]))
# print(students[1]>=(students[2]))
# print(students[1]>(students[2]))
# print(students[1]<(students[2]))
# print(students[1]<=(students[2]))

# students[0].add_grade(9)
# print(students[0].grads)

print(sorted(students, key=lambda student: student.average_grade(), reverse = True)) # сортировка по среднему баллу

for student in students:
    if student.average_grade() > 8:
        print(student.surname, float('{:.2f}'.format(student.average_grade())))

