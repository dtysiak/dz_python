#1 from hw9
import unittest
class Rhomb:
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a
        self.angle_b = 180 - angle_a

class TestRhomb(unittest.TestCase):
    def test_angles_sum(self):
        rhomb = Rhomb(side_a = 2, angle_a = 60)
        expected_result = 180
        actual_result = rhomb.angle_a + rhomb.angle_b
        print(f"Expected Result: {expected_result} | Actual Result: {actual_result}")
        self.assertEqual(expected_result, actual_result)

#2 from hw8
class Student:
    def __init__(self, name, age, average):
        self.name = name
        self.age = age
        self.average = average

class TestStudent(unittest.TestCase):
    def test_change_average(self):
        student = Student("Diana", 23, 10)
        expected_result = 10
        actual_result = student.average
        print(f"Expected Result: {expected_result} | Actual Result: {actual_result}")
        self.assertEqual(expected_result, actual_result)

#3 from hw7
def page_amount(photos_amount, photos_per_page_amount):
    return photos_amount//photos_per_page_amount

class TestPageAmount(unittest.TestCase):
    def test_page_amount(self):
      photos_amount = 232
      photos_per_page_amount = 8
      expected_result = 29
      actual_result =  page_amount(photos_amount, photos_per_page_amount)
      print(f"Expected Result: {expected_result} | Actual Result: {actual_result}")
      self.assertEqual(expected_result, actual_result)

#4 from hw7
def computer_price(month_amount, month_payment):
    return month_amount * month_payment

class TestComputerPrice(unittest.TestCase):
    def test_computer_price(self):
        month_amount = 18
        month_payment = 1179
        expected_result = 21222
        actual_result = computer_price(month_amount, month_payment)
        print(f"Expected Result: {expected_result} | Actual Result: {actual_result}")
        self.assertEqual(expected_result, actual_result)

#5 from hw7
def sum_sea(black_sea, azov_sea):
    return black_sea + azov_sea

class TestSum(unittest.TestCase):
    def test_sum_sea(self):
        black_sea = 436402
        azov_sea = 37800
        expected_result = 474202
        actual_result = sum_sea(black_sea, azov_sea)
        print(f"Expected Result: {expected_result} | Actual Result: {actual_result}")
        self.assertEqual(expected_result, actual_result)

#6 from hw7
def sum_numbers(a, b):
    return a + b

class TestSumm(unittest.TestCase):
    def test_sum_numbers(self):
        a = 5
        b = 6
        expected_result = 11
        actual_result = sum_numbers(a, b)
        print(f"Expected Result: {expected_result} | Actual Result: {actual_result}")
        self.assertEqual(expected_result, actual_result)

#7 from hw7
def sum_even_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total = total + num
    return total

class TestSumEven(unittest.TestCase):
    def test_sum_even(self):
        numbers = [1, 2, 3, 4]  # список чисел
        expected_result = 6
        actual_result = sum_even_numbers(numbers)
        print(f"Expected Result: {expected_result} | Actual Result: {actual_result}")
        self.assertEqual(expected_result, actual_result)


#8-10 from hw9
class Rhomb2:
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a
        self.angle_b = 180 - angle_a

class TestRhomb2(unittest.TestCase):
    def test_sum_of_angles(self):
        rhomb = Rhomb2(5, 60)
        expected_result = 180
        actual_result = rhomb.angle_a + rhomb.angle_b
        print(f"Expected Result: {expected_result} | Actual Result: {actual_result}")
        self.assertEqual(expected_result, actual_result)

    def test_angle_b_value(self):
        rhomb = Rhomb2(5, 60)
        expected_result = 120
        actual_result = rhomb.angle_b
        print(f"Expected Result: {expected_result} | Actual Result: {actual_result}")
        self.assertEqual(expected_result, actual_result)

    def test_side_a_value(self):
        rhomb = Rhomb2(5, 60)
        expected_result = 5
        actual_result = rhomb.side_a
        print(f"Expected Result: {expected_result} | Actual Result: {actual_result}")
        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    unittest.main()



