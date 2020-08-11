
class Calc:

    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        return num1 / num2

    def in_cm(self, num1):
        return num1 * 2.54

    def cm_in(self, num1):
        return num1 / 2.54


simple_calc = Calc()
print(simple_calc)  # <__main__.Calculator object at 0x00000231C9D17400>
print(simple_calc.add(2, 2))  # 4
print(simple_calc.subtract(3, 1))  # 2
print(simple_calc.multiply(3, 3))  # 9
print(simple_calc.divide(12, 6))  # 2
print(simple_calc.in_cm(5))  # 12.7
print(simple_calc.cm_in(12.7))  # 5.0



