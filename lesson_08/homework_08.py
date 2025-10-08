# Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
# Створіть об'єкт цього класу, представляючи студента.
# Потім додайте метод до класу "Студент", який дозволяє змінювати середній бал студента.
# Виведіть інформацію про студента та змініть його середній бал.

class Student:
    def __init__(self, first_name, second_name, age, average):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age
        self.average = average

    def display(self):
        print(f"First Name of student: {self.first_name}")
        print(f"Second name of student: {self.second_name}")
        print(f"Age of student: {self.age}")
        print(f"Average of student: {self.average}")

    def change_average(self, new_average):
        self.average = new_average
        print(f"Average of student: {self.average}")

first_student = Student("Diana", "Tysiak", "23", "10")
first_student.display
first_student.change_average("11")
first_student.display()

