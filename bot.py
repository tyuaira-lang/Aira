import telebot

TOKEN = "8491565022:AAE1pM4TWN4BbZ8brr9Dtjy8Dy5b1_vdGu0"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام! ربات روشن شد ✅")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()
