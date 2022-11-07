from telebot import types
# библиотека работы с гугл таблицами
import gspread
# библиотека проверки даты
from datetime import *
# библиотека рандома
from random import *


def marks_buttons(bot, message):  # функция определяющая клавиатуру с марками авто
    kb1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    but1 = types.KeyboardButton(text='🔘 Клюшки')
    but2 = types.KeyboardButton(text='🔘 Коньки')
    but3 = types.KeyboardButton(text='🔘 Защита')
    but4 = types.KeyboardButton(text='🔘 Вратарям')
    but5 = types.KeyboardButton(text='🔘 Другое')
    kb1.add(but1, but2, but3, but4, but5)
    bot.send_message(message.chat.id, 'Пожалуйста выберите подкатегорию', reply_markup=kb1)


class model_buttons:  # класс формирования клавиатур

    def __init__(self, bot, message, **kwargs):
        self.bot = bot
        self.message = message
        self.kwargs = kwargs

    def model_buttons(self):
        kb3 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        for key, value in self.kwargs.items():
            key = types.KeyboardButton(text=f'{value}')
            kb3.add(key)
        self.bot.send_message(self.message.chat.id, 'Пожалуйста выберите подкатегорию', reply_markup=kb3)

    def zayavka_buttons(self):
        kb4 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        but1 = types.KeyboardButton(text='Да, хочу!')
        but2 = types.KeyboardButton(text='🔙Вернуться в начало')
        kb4.add(but1, but2)
        self.bot.send_message(self.message.chat.id, f'Хотите оформить заявку на выбранный товар?\n'
                                                    f'/help - справка по боту\n', reply_markup=kb4)


def zayavka_done(bot, message, tovar_name):
    kb2 = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, f'Заявка оформлена и передана менеджеру, с Вами свяжутся в ближайшее время. '
                                      'Спасибо, что выбрали нас.🤝\n'
                                      f'Чтобы продолжить покупки воспользуйтесь командой /category', reply_markup=kb2)
    bot.send_message('1338281106', f'🚨!!!ВНИМАНИЕ!!!🚨\n'
                                   f'Поступила ЗАЯВКА от:\n'
                                   f'Имя: {message.from_user.first_name}\n'
                                   f'Фамилия: {message.from_user.last_name}\n'
                                   f'Ссылка: @{message.from_user.username}\n'
                                   f'Товар: {tovar_name}'
                                   f'\n')
    poisk_tovar_in_base(bot, message, tovar_name).zayavka_v_baze()


class poisk_tovar_in_base:
    def __init__(self, bot, message, tovar_name):
        self.bot = bot
        self.message = message
        self.tovar_name = tovar_name
        gc = gspread.service_account(filename='pidor-of-the-day-af3dd140b860.json')  # доступ к гугл табл по ключевому файлу аккаунта разраба
        # открытие таблицы по юрл адресу:
        sh = gc.open('CCN')
        self.worksheet = sh.worksheet('остатки')  # выбор листа 'общая база клиентов' таблицы
        self.worksheet2 = sh.worksheet('заявки')
        self.cell = self.worksheet.find(self.tovar_name)  # поиск ячейки с данными по ключевому слову

    def poisk_ostatok(self):
        try:
            self.bot.send_message(self.message.chat.id, 'Проверяем наличие..')
            # запись клиента в свободную строку базы старых клиентов:
            if self.tovar_name == 'Красная лента (N SZ)':
                file_open = open("red tape.png", 'rb')
                opisanie = 'Описвание: ЛЕНТА FLEXTAPE CCM 4,5MX38MM RD\nЦена: 500Р'
            if self.tovar_name == 'Красная лента (L)':
                file_open = open("red tape.png", 'rb')
                opisanie = 'Описание: ЛЕНТА FLEXTAPE CCM 4,5MX38MM RD\nЦена: 500Р'
            if self.tovar_name == 'Черная лента (L)':
                file_open = open("black tape.png", 'rb')
                opisanie = 'Описание: ЛЕНТА FLEXTAPE CCM 4,5MX38MM BD\nЦена: 500Р'
            if self.tovar_name == 'Черная лента (N SZ)':
                file_open = open("black tape.png", 'rb')
                opisanie = 'Описание: ЛЕНТА FLEXTAPE CCM 4,5MX38MM BD\nЦена: 500Р'
            self.bot.send_photo(self.message.chat.id, file_open, opisanie)
            self.bot.send_message(self.message.chat.id, f' В наличии: {self.worksheet.cell(self.cell.row, 5).value}\n')
            if self.worksheet.cell(self.cell.row, 5).value == '0':
                kb4 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
                but1 = types.KeyboardButton(text='🔙Вернуться в начало')
                kb4.add(but1)
                self.bot.send_message(self.message.chat.id, f'Увы товар закончился\n'
                                                            f'/help - справка по боту\n', reply_markup=kb4)
            else:
                model_buttons(self.bot, self.message).zayavka_buttons()
        except AttributeError:
            self.bot.send_message(self.message.chat.id, 'Ошибка, товар отсутствует')

    def zayavka_v_baze(self):  # функция перевода из базы потенциальных клиентов в базу старых клиентов
        try:
            worksheet_len2 = len(self.worksheet2.col_values(2)) + 1
            # запись клиента в свободную строку базы старых клиентов:
            self.worksheet2.update(f'A{worksheet_len2}:G{worksheet_len2}',
                                   [[self.message.chat.id, self.message.from_user.username,
                                     self.message.from_user.first_name, self.message.from_user.last_name,
                                     self.tovar_name, 'none', str(datetime.now().date())]])
            update_ostatok = int(self.worksheet.cell(self.cell.row, 5).value) - 1
            self.worksheet.update(f"E{self.cell.row}", [[update_ostatok]])  # удаление клиента из базы потенциальных
            update_zakaz = int(self.worksheet.cell(self.cell.row, 4).value) + 1
            self.worksheet.update(f"D{self.cell.row}", [[update_zakaz]])  # удаление клиента из базы потенциальных
            self.bot.send_message('1338281106', 'Заявка внесена в базу ✅\n'
                                                'смотреть базу: https://docs.google.com/spreadsheets/d/'
                                                '14P5j3t4Z9kmy4o87WEbLqeTwsKi7YZAx7RiQPlY2c1w/edit?usp=sharing')
        except AttributeError:
            self.bot.send_message('1338281106', 'Ошибка! Не удается добавить заказ в базу')


class tovar:  # класс хранения сообщения для рассылки
    def __init__(self, tovar):
        self.tovar = tovar

    def _get_tovar_(self):
        return self.tovar
