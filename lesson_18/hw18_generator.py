# Напишіть генератор, який повертає послідовність парних чисел від 0 до N.

def even_numbers(numbers):
    for num in numbers:
        if num % 2 == 0:
            yield num

print(list(even_numbers([1,2,3,4,5,6,7,8,9])))

# Створіть генератор, який генерує послідовність Фібоначчі до певного числа N.

def fibonacci_num(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

print(list(fibonacci_num(100)))
