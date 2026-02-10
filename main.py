import os
import unittest
print(os.path.abspath(__file__))
def calculator():
    print("Калькулятор активовано")
    num1_vvid = (input("Введіть перше число: ").strip().replace("," , "."))
    alphavit = "йцукенгшщзхїфівапролджєґячсмитьюqwertyuiopasdfghjklzxcvbnm"
    liters = False
    for symbol in num1_vvid.lower():
        if symbol in alphavit:
            liters = True
            break
    if liters:
        print("Помилка ти ввів літери")
        return
    num1 = float(num1_vvid)
    operator = (input("Оберіть дію (+, -, *, /):") .strip())
    num2_vvid = (input("Введіть друге число: ").strip().replace("," , "."))
    for symbol in num2_vvid.lower():
        if symbol in alphavit:
            liters = True
            break
    if liters:
        print("Помилка ти ввів літери")
        return
    num2 = float(num2_vvid)
    if operator == '+': 
        result = num1 + num2
    elif operator == '-': 
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/': 
        result = num1 / num2 if num2 != 0 else "Помилка: ділення на нуль"
    else:
        result = "Невідома операція"

    output = f"{num1} {operator} {num2} = {result}"
    print(output)
    fille = open("results.txt", "a" , encoding="utf-8")
    fille.write(output + "\n")
    fille.close()

calculator() 
def sum(a, b): 
    return a + b
def minus(a, b): 
    return a - b
def mul(a, b): 
    return a * b
def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Помилка: ділення на нуль"
class testcalculator(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(sum(10, 20), 30)
        self.assertEqual(sum(-1, 1), 0)
    def test_minus(self):
        self.assertEqual(minus(20, 10), 10)
        self.assertEqual(minus(2, 1), 1)
unittest.TestProgram()  