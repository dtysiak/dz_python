# Реалізуйте ітератор для зворотного виведення елементів списку.

class Itarator_reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        num = self.data[self.index]
        self.index -= 1
        return num

for k in Itarator_reverse([1, 2, 3, 4, 5]):
    print(k)

# Напишіть ітератор, який повертає всі парні числа в діапазоні від 0 до N.

class Iterator_even_numbers:
    def __init__(self, data):
        self.data = data
    def __init__(self, n):
        self.n = n
        self.current = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current > self.n:
            raise StopIteration

        num2 = self.current
        self.current += 2
        return num2

for k in Iterator_even_numbers(10):
    print(k)

