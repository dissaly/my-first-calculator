def calculator():
    print("--- Калькулятор активовано ---")
    try:
        num1 = float(input("Введіть перше число: "))
        operator = input("Оберіть дію (+, -, *, /): ")
        num2 = float(input("Введіть друге число: "))

        if operator == '+': result = num1 + num2
        elif operator == '-': result = num1 - num2
        elif operator == '*': result = num1 * num2
        elif operator == '/': 
            result = num1 / num2 if num2 != 0 else "Помилка: ділення на нуль"
        else: result = "Невідома операція"

        output = f"{num1} {operator} {num2} = {result}"
        print(output)

        # Збереження у файл
        with open("results.txt", "a", encoding="utf-8") as file:
            file.write(output + "\n")
        print("Результат додано у results.txt")

    except ValueError:
        print("Помилка: треба вводити тільки числа!")

if __name__ == "__main__":
    calculator()