import telebot
from telebot import types
from config import TOKEN


bot = telebot.TeleBot(TOKEN)




menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
menu.row("Супы🍲","Горячие блюда🍛")
menu.row("Десерты🍰","Напитки🥤")


@bot.message_handler(commands=['start'])


def start(message):
    

    bot.send_message(message.chat.id,"Добро пожаловать в наш ресторона,для вас доступно электронное меню",reply_markup=menu)



@bot.message_handler(func=lambda message:True)

def second(message):
    dish = types.ReplyKeyboardMarkup(resize_keyboard=True)
    dish.row("Блюдо 1","Блюдо 2","Блюдо 3")
    dish.row("🔙Вернуться в меню")
    if message.text == "Супы🍲":
        bot.send_message(message.chat.id,"Выберите суп",reply_markup=dish)
    elif message.text == "Горячие блюда🍛":
        bot.send_message(message.chat.id,"Выберите горячее блюдо",reply_markup=dish)
    elif message.text == "Десерты🍰":
        bot.send_message(message.chat.id,"Выберите десерт",reply_markup=dish)
    elif message.text == "Напитки🥤":
        bot.send_message(message.chat.id,"Выберите напиток",reply_markup=dish)
    elif message.text == "🔙Вернуться в меню":
        bot.send_message(message.chat.id,"Идем в меню",reply_markup=menu)
    elif message.text in ["Блюдо 1","Блюдо 2","Блюдо 3"]:
        bot.send_message(message.chat.id,f"вы выбрали {message.text}")
        





bot.polling(non_stop=True)