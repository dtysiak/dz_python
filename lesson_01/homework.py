# task 01 == Виправте синтаксичні помилки
print("Hello", end=" ")
print("world!")



# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
    print(hello, world)

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
banana = apples * 4
print('Aplles:', apples)
print ('Banana:', banana)

# task 05 == виправте назви змінних
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4
print('Storona 1:', storona_1)
print('Storona 2:', storona_2)
print('Storona 3:', storona_3)
print('Storona 4:', storona_4)

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4
perimetery = storona_1 + storona_2 + storona_3 + storona_4
print(perimetery)



    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі

# task 07

### У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
### Скільки всього дерев посадили в саду?
apples = 4
pears = 4+5
plums = 4-2
trees = apples + pears + plums
print("В саду посадили", trees, "дерев")

# task 08

###До обіда температура повітря була на 5 градусів вище нуля.
###Після обіду температура опустилася на 10 градусів.
###Надвечір потепліло на 4 градуси. Яка температура надвечір?
morning_temp = 5
afternoon_temp = morning_temp - 10
evening_temp = afternoon_temp + 4
print("До обіду було", morning_temp , "градусів.️")
print("Після обіду температура опустилась до", afternoon_temp , "градусів.")
print("Надвечір температура була", evening_temp , "градус.")

# task 09

###Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
###1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
###Скількі сьогодні дітей у театральному гуртку?
boys = 24
girls = 24//2
boys_today = boys - 1
girls_today = girls - 2
children_today = boys_today + girls_today
print('Cьогодні було', children_today, 'дітей у театральному гуртку')

# task 10

###Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
###а третя - як половина вартості першої та другої разом.
###Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
first_book = 8
second_book = 8+2
third_book = (first_book+second_book)//2
print('Перша книжка коштує', first_book, 'гривень')
print('Друга книжка коштує', second_book, 'гривень')
print('Третя книжка коштує', third_book, 'гривень')
print('Усі книги коштуватимуть в сумі',first_book+second_book+third_book, 'гривень')
