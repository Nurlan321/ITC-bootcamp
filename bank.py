import telebot
from bankbot import TOKEN
from telebot import types
from bankpars import a, b, c, d  

TOKEN = "6935134810:AAGcfvxKp2GhoRGtfC0p1ZN4eofUB6g34nk"
bot = telebot.TeleBot(TOKEN)
URL = "https://www.optimabank.kg/index.php?option=com_nbrates&view=default&Itemid=196&lang=ru"

menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
menu.row("Доллар", "Евро")
menu.row("Тенге", "Рубль")

@bot.message_handler(commands=['start', 'menu'])  
def start(message):
    bot.send_message(message.chat.id, "Выберите валюту:", reply_markup=menu)

@bot.message_handler(func=lambda message: True)
def second(message):
    if message.text in ["Доллар", "Евро", "Тенге", "Рубль"]:
        dish = types.ReplyKeyboardMarkup(resize_keyboard=True)
        dish.row("Вернуться в меню")
        if message.text == "Доллар":
            bot.send_message(message.chat.id, f"Курс доллара покупка: {a[0]}, продажа: {a[1]}", reply_markup=dish)
        elif message.text == "Евро":
            bot.send_message(message.chat.id, f"Курс евро покупка: {b[0]}, продажа: {b[1]}", reply_markup=dish)
        elif message.text == "Тенге":
            bot.send_message(message.chat.id, f"Курс тенге покупка: {c[0]}, продажа: {c[1]}", reply_markup=dish)
        elif message.text == "Рубль":
            bot.send_message(message.chat.id, f"Курс рубля покупка: {d[0]}, продажа: {d[1]}", reply_markup=dish)
    elif message.text == "Вернуться в меню":  
        start(message)
    else:
        bot.send_message(message.chat.id, "Пожалуйста, используйте кнопки на клавиатуре.")

bot.polling(non_stop=True)
