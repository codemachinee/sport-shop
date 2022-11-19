import json
import telebot
 #с помощью типов можно создавать клавиатуры
from telebot import types

token = '5380562272:AAFqodiUpENCtx7oD8f5xnbIDNOoxJW6YMY'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def marks_buttons(message):  # функция определяющая клавиатуру с марками авто
    keys = {}
    kb1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    file = open('categories_dict.json', 'rb')
    file = json.load(file)
    file = file['general_menu']
    for i in file:
        keys[f'but{file.index(i)}'] = types.KeyboardButton(text=i)
        kb1.add(keys[f'but{file.index(i)}'])
    print(kb1)
    bot.send_message(message.chat.id, 'Пожалуйста выберите подкатегорию', reply_markup=kb1)


bot.polling()
