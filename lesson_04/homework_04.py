adventures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""
print(adventures_of_tom_sawer.replace("\n", " "))

#ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
#task 01
#Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
#треба замінити кінець абзацу на пробіл .replace("\n", " ")"""

#task 02
#Замініть .... на пробіл
print(adventures_of_tom_sawer.replace("....", " "))


#task 03
#Зробіть так, щоб у тексті було не більше одного пробілу між словами.
print(adventures_of_tom_sawer.replace("  ", " "))


#task 04
#Виведіть, скількі разів у тексті зустрічається літера "h"
print(adventures_of_tom_sawer.count("h"))


#task 05
#Виведіть, скільки слів у тексті починається з Великої літери?
words = adventures_of_tom_sawer.split()
upper_letter = [word for word in words if word[0].isupper()]
print(len(upper_letter))


#task 06
#Виведіть позицію, на якій слово Tom зустрічається вдруге
text = adventures_of_tom_sawer
found = text.find("Tom", text.find ("Tom") +1)
if found != -1:
    print(f"Слово Tom вдруге зустрічається на позиції {found}")


#task 07
#Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
#Збережіть результат у змінній adwentures_of_tom_sawer_sentences
#adwentures_of_tom_sawer_sentences = None
adventures_of_tom_sawer_sentences = adventures_of_tom_sawer.replace("\n", " ")
adventures_of_tom_sawer_sentences = adventures_of_tom_sawer_sentences.replace("....", " ")
adventures_of_tom_sawer_sentences = adventures_of_tom_sawer_sentences.split('.')
print(adventures_of_tom_sawer_sentences)


#task 08
#Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
#Перетворіть рядок у нижній регістр.
text = adventures_of_tom_sawer.replace("\n", " ")
text = text.replace("....", " ")
text = text.split('.')
sentence = text[3].strip()
print("Четверте речення з тексту:", sentence)

lower_sentence = sentence.lower()
print(lower_sentence)


#task 09
#Перевірте чи починається якесь речення з "By the time".
sentences = adventures_of_tom_sawer.split('.')
found = False
for sentence in sentences:
    sentence = sentence.strip()
    if sentence.startswith("By the time"):
        found = True
if found:
    print("Є таке речення")
else:
    print("Нема такого речення")


#task 10
#Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
adventures_of_tom_sawer_sentences = adventures_of_tom_sawer.split('.')
for sentence in adventures_of_tom_sawer_sentences:
    sentence = sentence.strip()
    if sentence!= "":
     last_sentence = sentence
words = last_sentence.split()
print(f"Кількість слів останнього речення становить", len(words), ": morning, Tom was literally rolling in wealth")

