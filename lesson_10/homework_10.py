# Завдання 1
# Створіть клас Employee, який має атрибути name та salary.
# Далі створіть два класи, Manager та Developer, які успадковуються від Employee.
# Клас Manager повинен мати додатковий атрибут department, а клас Developer - атрибут programming_language.
# Клас TeamLead повинен мати всі атрибути як
# Manager (ім'я, зарплата, відділ), Developer(ім'я, зарплата, мова програмування),
# а також атрибут team_size, який вказує на кількість розробників у команді, якою керує керівник.

class Employee:
    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.salary = kwargs.get("salary")

class Manager(Employee):
    def __init__(self, **kwargs):
        Employee.__init__(self, **kwargs)
        self.department = kwargs.get("department")

class Developer(Employee):
    def __init__(self, **kwargs):
        Employee.__init__(self, **kwargs)
        self.programming_language = kwargs.get("programming_language")

class TeamLead(Manager, Developer):
    def __init__(self, **kwargs):
        Manager.__init__(self, **kwargs)
        Developer.__init__(self, **kwargs)
        self.team_size = kwargs.get("team_size")

lead = TeamLead(name = "Diana", salary = 3000, department = "QA Department", programming_language = "Python",team_size = 6)
print(f"Name: {lead.name}")
print(f"Salary: {lead.salary}")
print(f"Department: {lead.department}")
print(f"Programming language: {lead.programming_language}")
print(f"Team size: {lead.team_size}")

# Завдання 2
# Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру.
# Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично вірні для них методи для площі та периметру.
# Властивості по типу “довжина сторони” й т.д. повинні бути приватними, та ініціалізуватись через конструктор.
# Створіть Декілька різних об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу та периметр кожної.
# Створіть Декілька різних об’єктів фігур, та у циклі порахуйте та виведіть в консоль площу та периметр кожної.

from abc import ABC, abstractmethod

class Figure(ABC):
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius
    def get_area(self):
        return 3.14 * self.__radius ** 2
    def get_perimeter(self):
        return 2 * 3.14 * self.__radius

class Rectangle(Figure):
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
    def get_area(self):
        return self.__width * self.__height
    def get_perimeter(self):
        return 2 * (self.__width + self.__height)

class Square(Figure):
    def __init__(self, side):
        self.__side = side
    def get_area(self):
        return self.__side ** 2
    def get_perimeter(self):
        return 4 * self.__side

shapes = [Circle(2), Rectangle(2, 2), Square(2)]
for shape in shapes:
    print(f"{shape.__class__.__name__}:")
    print("Площа =", shape.get_area())
    print("Периметр =", shape.get_perimeter())
    print()

