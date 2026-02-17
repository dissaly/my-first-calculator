import os


print(os.path.abspath(__file__))


def calculator():

    print("Калькулятор активовано")

    try:

        num1 = float(input("Введіть перше число: ").strip())
        operator = input("Введіть +,-,*,/: ").strip()
        num2 = float(input("Введіть друге число: ").strip())

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            result = num1 / num2 if num2 != 0 else "Помилка: ділення на нуль"

        output = f"{num1} {operator} {num2} = {result}"
        print(output)

        file = open("results.txt", "a", encoding="utf-8")
        file.write(output + "\n")
        file.close()

    except:
        print("Помилка ти ввій невідомий символ")


calculator()
