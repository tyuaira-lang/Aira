import telebot
import os

TOKEN = os.getenv("BOT_TOKEN")  # توکن از Environment Variables گرفته میشه
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "سلام! ربات روشن شد ✅")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()
