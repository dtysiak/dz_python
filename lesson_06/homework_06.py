# Порахувати кількість унікальних символів в строці.
# Якщо їх більше 10 - вивести в консоль True, інакше - False.
# Строку отримати за допомогою функції input()

string = input('Enter your value:')
unique_characters = []
for character in string:
    if character not in unique_characters:
        unique_characters.append(character)

if len(unique_characters) > 10:
    print(True)
else:
    print(False)

# Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h"
# (враховуються як великі так і маленькі).
# Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".

word = ""
while "h" not in word and "H" not in word:
    word = input("Enter the word with letter 'h/H': ")
    if "h" in word or "H" in word:
        print("Success")
    else:
        print("Try again.")

# Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг, які присутні в lst1.
# Данні в лісті можуть бути будь якими

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = []
for value in lst1:
    if value == str(value):
        lst2.append(value)
print(lst2)

# Є лист з числами, порахуйте суму усіх ПАРНИХ чисел в цьому листі

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_numbers = 0
for num in numbers:
    if num % 2 == 0:
        sum_numbers = sum_numbers + num
print(sum_numbers)