# Напишіть декоратор, який логує аргументи та результати викликаної функції.

def logging(func):
    def wrapper(*args):
        print(f"Аргументи: {args}")
        result = func(*args)
        print(f"Результати: {result}")
        return result
    return wrapper

@logging
def sum(a, b):
    return a + b
sum(2, 2)

# Створіть декоратор, який перехоплює та обробляє винятки, які виникають в ході виконання функції.

def fails(func):
    def wrapper(*args):
        try:
            return func(*args)
        except Exception as error:
            print(f"Error occurred: {error}")
    return wrapper

@fails
def division(a, b):
    return a/b
division(5, 0)

