# task 1
# Задача - надрукувати табличку множення на задане число, але
# лише до максимального значення для добутку - 25.
# Код майже готовий, треба знайти помилки та випраавити\доповнити.
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1
    result = 0

    # Complete the while loop condition.
    while result <= 25:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
# Написати функцію, яка обчислює суму двох чисел.
def sum_numbers(a, b):
     return a+b

print (sum_numbers(2, 2))


# task 3
# Написати функцію, яка розрахує середнє арифметичне списку чисел.

def average(numbers):
    all_numbers = sum(numbers)
    return all_numbers/len(numbers)

print(average([1, 2, 3, 4, 5]))



# task 4
# Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
def reverse(string):
    return string[::-1]

print(reverse("Diana"))


# task 5
# Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
def longest_word(list_of_words):
    return max(list_of_words, key=len)

list_of_words = ["Python", "Diana", "Course", "Lviv"]
print(longest_word(list_of_words))


# task 6
# Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
# у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
# не є підрядком першого рядка.
def find_substring(str1, str2):
    index =  str1.find(str2)
    return index

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# Оберіть будь-які 4 таски з попередніх домашніх робіт та
# перетворіть їх у 4 функції, що отримують значення та повертають результат.
# Обоязково документуйте функції та дайте зрозумілі імена змінним.

# task 7

# from homework_06
# Є лист з числами, порахуйте суму усіх ПАРНИХ чисел в цьому листі
def sum_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total = total + num
    return total

print(sum_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


# task 8

# from homework_03
# Площа Чорного моря становить 436 402 км2, а площа Азовського
# моря становить 37 800 км2. Яку площу займають Чорне та Азов-ське моря разом?
def sum_sea(black_sea, azov_sea):
    return black_sea + azov_sea

black_sea = 436402
azov_sea = 37800
print(f"Чорне та Азовське моря разом займають", sum_sea(black_sea, azov_sea), "км2.")


# task 9

# from homework_03
# Михайло разом з батьками вирішили купити комп’ютер, ско-
# риставшись послугою «Оплата частинами». Відомо, що сплачу-
# вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
# вартість комп’ютера.
def computer_price(month_amount, month_payment):
    return month_amount * month_payment

month_amount = 18
month_payment = 1179
print (f"Вартість комп'ютера становить {computer_price(month_amount, month_payment):,} грн." .replace(",", " "))


# task 10

# from homework_03
# Ігор займається фотографією. Він вирішив зібрати всі свої 232
# фотографії та вклеїти в альбом. На одній сторінці може бути
# розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
# Ігорю, щоб вклеїти всі фото?
def page_amount(photos_amount, photos_per_page_amount):
    return photos_amount//photos_per_page_amount

photos_amount = 232
photos_per_page_amount = 8
print(f"Ігорю знадобиться {page_amount(photos_amount, photos_per_page_amount)}"+ " сторінок, щоб вклеїти всі фото.")