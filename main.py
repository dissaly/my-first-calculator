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
        "Привіт! Я супер-калькулятор. 🧮\nЯ розумію коми, крапки та навіть приклади з дужками!",
    )


@bot.message_handler(content_types=["text"])
def calculate(message):
    try:

        user_input = (
            message.text.replace(",", ".")
            .replace("×", "*")
            .replace("%", "/100")
            .replace("[", "(")
            .replace("]", ")")
            .replace(":", "/")
        )

        result = eval(user_input)

        output = f"Результат: {result}"
        bot.reply_to(message, output)

        with open("results.txt", "a", encoding="utf-8") as file:
            file.write(f"{user_input} = {result}\n")

    except ZeroDivisionError:
        bot.reply_to(message, "Помилка: на нуль ділити не можна! ❌")
    except Exception:
        bot.reply_to(
            message, "Не можу це порахувати. Пиши приклади цифрами, наприклад: (2+3)*4"
        )


@bot.message_handler(
    content_types=["photo", "audio", "voice", "video", "document", "sticker"]
)
def handle_media(message):
    bot.reply_to(message, "Гарна спроба! Але я працюю тільки з текстом і цифрами. 😉")


print("Бот запущений і готовий до тестів...")
bot.infinity_polling()
