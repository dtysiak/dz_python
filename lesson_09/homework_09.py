# Створіть клас геометричної фігури "Ромб". Клас повинен мати наступні атрибути:
# сторона_а (довжина сторони a).
# кут_а (кут між сторонами a і b).
# кут_б (суміжний з кутом кут_а).
# Необхідно реалізувати наступні вимоги:
# Значення сторони сторона_а повинно бути більше 0.
# Кути кут_а та кут_б повинні задовольняти умову: кут_а + кут_б = 180
# Протилежні кути ромба завжди рівні, тому при заданому значенні кут_а, значення кут_б обчислюється автоматично.
# Для встановлення значень атрибутів використовуйте метод __setattr__.

class Rhomb:
    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a
        self.angle_b = 180 - angle_a

    def __setattr__(self, name, value):
        if name == "side_a":
            if value <= 0:
                print("Side_a must be positive value")
                value = 1

        if name == "angle_a":
            if value <= 0 or value >= 180:
                print("Angle_a and angle_b must be 180")
                value = 60
            self.__dict__["angle_b"] = 180 - value

        if name == "angle_b":
            if value <= 0 or value >= 180:
                print("Angle_a and angle_b must be 180")
                value = 120
            self.__dict__["angle_a"] = 180 - value
        self.__dict__[name] = value

    def info(self):
        print(f"Side_a = {self.side_a}, angle_a = {self.angle_a}, angle_b = {self.angle_b}")

romb1 = Rhomb(5, 60)
romb1.info()















