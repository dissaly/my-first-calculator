import telebot

import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(message):

    bot.reply_to(
        message,
        "Привіт! Я безпечний калькулятор. 🧮\nНапиши мені приклад, наприклад: 5+5 або 10/2",
    )


@bot.message_handler(content_types=["text"])
def calculate(message):

    try:

        user_input = message.text.replace(" ", "").replace(",", ".")

        num1 = ""

        num2 = ""

        operator = ""

        found_operator = False  #

        for char in user_input:

            if char in "0123456789.":

                if not found_operator:

                    num1 += char

                else:

                    num2 += char

            elif char in "+-*/×: ":

                if char == "×":

                    operator = "*"

                elif char == ":":

                    operator = "/"

                else:

                    operator = char

                found_operator = True

        a = float(num1)

        b = float(num2)

        result = 0

        if operator == "+":

            result = a + b

        elif operator == "-":

            result = a - b

        elif operator == "*":

            result = a * b

        elif operator == "/":

            if b == 0:

                raise ZeroDivisionError

            result = a / b

        if result == int(result):

            result = int(result)

        output = f"Результат: {result}"

        bot.reply_to(message, output)

        with open("results.txt", "a", encoding="utf-8") as file:

            file.write(f"{num1} {operator} {num2} = {result}\n")

    except ZeroDivisionError:

        bot.reply_to(message, "Помилка: на нуль ділити не можна! ❌")

    except Exception:

        bot.reply_to(
            message, "Не можу це порахувати. Пиши прості приклади, як-от: 12+4"
        )


@bot.message_handler(
    content_types=["photo", "audio", "voice", "video", "document", "sticker"]
)
def handle_media(message):

    bot.reply_to(message, "Я працюю тільки з текстом і цифрами. 😉")


print("Бот запущений з використанням 'operator'...")

bot.infinity_polling()
