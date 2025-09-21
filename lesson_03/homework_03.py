alice_in_wonderland = ( '"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," - said the Cat.\n'
    '"I don`t much care where" - said Alice.\n'
'"Then it doesn`t matter which way you go," - said the Cat.\n'
'"- so long as I get somewhere," - Alice added as an explanation.\n'
'"Oh, you`re sure to do that," - said the Cat - "if you only walk long enough."'
)
print(alice_in_wonderland)
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк



    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі

# task 04

#Площа Чорного моря становить 436 402 км2, а площа Азовського
#моря становить 37 800 км2. Яку площу займають Чорне та Азов-ське моря разом?
black_sea = 436402
azov_sea = 37800
sum_sea = (black_sea + azov_sea)
print(f"Чорне та Азовське моря разом займають {sum_sea:,} км²".replace(",", " "))


# task 05

#Мережа супермаркетів має 3 склади, де всього розміщено
#375 291 товар. На першому та другому складах перебуває
#250 449 товарів. На другому та третьому – 222 950 товарів.
#Знайдіть кількість товарів, що розміщені на кожному складі.

all_storage = 375291
first_second_storage = 250449
second_third_storage = 222950
first_storage = all_storage - second_third_storage
third_storage = all_storage - first_second_storage
second_storage = all_storage - first_storage - third_storage
print(f"На першому складі розміщено {first_storage:,}" .replace(",", " ") + " товарів")
print(f"На другому складі розміщено {second_storage:,}" .replace(",", " ") + " товарів")
print(f"На третьому складі розміщено {third_storage:,}" .replace(",", " ") + " товарів")


# task 06

#Михайло разом з батьками вирішили купити комп’ютер, ско-
#риставшись послугою «Оплата частинами». Відомо, що сплачу-
#вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
#вартість комп’ютера.
month_amount = 18
month_payment = 1179
computer_price = month_amount * month_payment
print(f"Вартість комп`ютера становить {computer_price:,}" .replace(",", " ") + " гривень")


# task 07

# Знайди остачу від ділення чисел:
# a) 8019 : 8     d) 7248 : 6
# b) 9907 : 9     e) 7128 : 5
# c) 2789 : 5     f) 19224 : 9

a_value = 8019%8
print(f"Остача від ділення 8019 на 8 дорівнює {a_value}")
b_value = 9907%9
print(f"Остача від ділення 9907 на 9 дорівнює {b_value}")
c_value = 2789%5
print(f"Остача від ділення 2789 на 5 дорівнює {c_value}")
d_value = 7248%6
print(f"Остача від ділення 7248 на 6 дорівнює {d_value}")
e_value = 7128%5
print(f"Остача від ділення 7128 на 5 дорівнює {e_value}")
f_value = 19224%9
print(f"Остача від ділення 19224 на 9 дорівнює {f_value}")


# task 08

# Іринка, готуючись до свого дня народження, склала список того,
# що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
# для даного її замовлення.
# Назва товару    Кількість   Ціна
# Піца велика     4           274 грн
# Піца середня    2           218 грн
# Сік             4           35 грн
# Торт            1           350 грн
# Вода            3           21 грн
pizza_big_amount = 4
pizza_big_price = 274
pizza_medium_amount = 2
pizza_medium_price = 218
juice_amount = 4
juice_price = 35
cake_amount = 1
cake_price = 350
water_amount = 3
water_price = 21

pizza_big_sum = pizza_big_amount*pizza_big_price
pizza_medium_sum = pizza_medium_amount*pizza_medium_price
juice_sum = juice_amount*juice_price
cake_sum = cake_amount*cake_price
water_sum = water_amount*water_price

final_sum = pizza_big_sum + pizza_medium_sum + juice_sum + cake_sum + water_sum
print(f"Іринці знадобиться {final_sum:,}" .replace(",", " ")+" гривень для її замовлення")


# task 09

# Ігор займається фотографією. Він вирішив зібрати всі свої 232
# фотографії та вклеїти в альбом. На одній сторінці може бути
# розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
# Ігорю, щоб вклеїти всі фото?
photos_amount = 232
photos_per_page_amount = 8
page_amount = photos_amount//photos_per_page_amount
print(f"Ігорю знадобиться {page_amount}"+ " сторінок, щоб вклеїти всі фото")


# task 10

# Родина зібралася в автомобільну подорож із Харкова в Буда-
# пешт. Відстань між цими містами становить 1600 км. Відомо,
# що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
# становить 48 літрів.
# 1) Скільки літрів бензину знадобиться для такої подорожі?
# 2) Скільки щонайменше разів родині необхідно заїхати на зап-
# равку під час цієї подорожі, кожного разу заправляючи пов-
# ний бак?
distance = 1600
fuel_per_100 = 9
fuel_capacity = 48
fuel_amount = distance//100 * fuel_per_100
stops = fuel_amount//fuel_capacity
print(f"Для подорожі знадобиться {fuel_amount}"+" літри")
print(f"Родині знадобиться заїхати на заправку {stops}"+" рази")