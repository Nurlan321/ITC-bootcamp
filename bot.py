#from confik import TOKEN 
import telebot
from telebot import types



bot = telebot.TeleBot('6918122290:AAE8IPrW4PAiGJMRYr8KVZ_xwgHmO8pPR9Y')


@bot.message_handler(commands=['start'])

def welcome(message):
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    b1 = types.KeyboardButton("Cars")
    b2 = types.KeyboardButton("About us")
    b3 = types.KeyboardButton("Contact")
    menu.add(b1,b2,b3)
    bot.send_message(message.chat.id,"Welcome to 'Auto-Trade", reply_markup=menu)

bot.polling(non_stop=True)
