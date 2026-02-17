import unittest
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