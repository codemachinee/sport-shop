import telebot
from telebot import types
import json
bot = telebot.TeleBot('5380562272:AAFqodiUpENCtx7oD8f5xnbIDNOoxJW6YMY')


@bot.message_handler(commands=['start'])
def start(message):  # функция создающая клавиатуру
    buttons(bot, message, 'general_menu', 'категорию',
            'https://i.gifer.com/U69E.gif').marks_buttons()


class buttons:  # класс для создания клавиатур различных категорий товаров
    def __init__(self, bot, message, key, kategoriya, image):
        self.bot = bot
        self.message = message
        self.file = open('categories_dict.json', 'rb')  # файл хранящий структуру категорий товаров
        self.file = json.load(self.file)  # открытие файла
        self.file = self.file[key]  # выбор в файле конкретной категории по ключу (возвращает список)
        self.kategoriya = kategoriya  # уровень меню (категории/подкатегории/товары)
        self.image = image

    def marks_buttons(self):  # функция создающая клавиатуру
        keys = {}
        kb1 = types.InlineKeyboardMarkup()
        for i in self.file:
            keys[f'but{self.file.index(i)}'] = types.InlineKeyboardButton(text=i, callback_data=i)
            if self.file.index(i) > 0 and self.file.index(i) % 2 != 0:
                kb1.add(keys[f'but{self.file.index(i)-1}'], keys[f'but{self.file.index(i)}'], row_width=2)
            elif self.file.index(i) == (len(self.file) - 1):
                kb1.add(keys[f'but{self.file.index(i)}'])
        self.bot.send_animation(self.message.chat.id, animation=self.image)
        self.bot.send_message(self.message.chat.id, text=f'Пожалуйста выберите {self.kategoriya}', reply_markup=kb1)


bot.polling()