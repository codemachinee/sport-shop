# библиотека телеграм-бота
import telebot
# с помощью типов можно создавать клавиатуры
from telebot import types
# библиотека для выполнения фоновых процессов в определенное время
#from apscheduler.schedulers.background import BackgroundScheduler
# импорт из файла functions
import json
from openpyxl import workbook, worksheet, load_workbook
from test_functions import buttons, zayavka_done, poisk_tovar_in_base, rasylka_message, admin_id, file,\
    platezhy
from passwords import *
import asyncio
article = None

token = code_mashine
#token = lemonade
bot = telebot.TeleBot(token)

tovar_name = None
quantity = None
rassylka = None


@bot.message_handler(commands=['start'])    # перехватчик команды /start
def start(message):
    file_open = open("start_logo.png", 'rb')    # открытие и чтение файла стартовой картинки
    bot.send_photo(message.chat.id, file_open, '''Здравствуйте!
Вас приветствует бот CCM_Club.
Я помогу подобрать хоккейный инвентарь из наличия по лучшим ценам. 🏆🏒🥇

Выберите «Каталог 🗂️» для просмотра товаров.
«О нас» расскажет вам о нас и как мы работаем.
Команда в строке /help – о всех возможностях бота.
''')
    buttons(bot, message).menu_buttons()


@bot.message_handler(commands=['help'])
def help(message):
    kb2 = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, '...', reply_markup=kb2)
    if message.chat.id == admin_id:      # условия демонстрации различных команд для админа и клиентов
        bot.send_message(message.chat.id, f'Основные команды поддерживаемые ботом:\n'
                                          f'  - для просмотра ассортимента по категориям\n'
                                          f'/start - инициализация бота\n'
                                          f'/help - справка по боту\n'
                                          f'/sent_message - отправить с помощью бота сообщение клиенту по id чата')
    else:
        bot.send_message(message.chat.id, f'Основные команды поддерживаемые ботом:\n'
                                          f'Выберите "Категории товаров 🗂️" - для просмотра ассортимента по категориям\n'
                                          f'/start - инициализация бота\n'
                                          f'/help - справка по боту\n')


@bot.message_handler(commands=['sent_message'])  # команда для переброски клиента из базы потенциальных клиентов в
def sent_message(message):    # базу старых клиентов
    if message.chat.id == admin_id:
        sent = bot.send_message(admin_id, 'Введи id чата клиента, которому нужно написать от лица бота')
        bot.register_next_step_handler(sent, sent_message_perehvat_1)   # перехватывает ответ пользователя на сообщение "sent" и
                                                              # и направляет его аргументом в функцию base_perehvat
    else:
        bot.send_message(message.chat.id, 'У Вас нет прав для использования данной команды')


@bot.message_handler(func=lambda m: m.text)  # перехватчик текстовых сообщений
def chek_message_category(m):
    list_one = []
    wb = load_workbook('CCM.xlsx')
    ws = wb['МЛ Остатки штаб']
    if m.text == 'Каталог 🗂️':
        for row in ws.iter_rows(min_row=2, min_col=9, max_col=9, values_only=True):
            if row == (None,):
                break
            list_one.append(*row)
        list_one = list(set(list_one))
        file_open = open("menu_logo.jpeg", 'rb')
        buttons(bot, m, kategoriya='раздел', list_one=list_one,
                image=file_open).razdely_buttons()
    elif m.text == "Вернуться в начало":
        for row in ws.iter_rows(min_row=2, min_col=9, max_col=9, values_only=True):
            if row == (None,):
                break
            list_one.append(*row)
        list_one = list(set(list_one))
        file_open = open("menu_logo.jpeg", 'rb')
        buttons(bot, m, kategoriya='раздел', list_one=list_one,
                image=file_open).razdely_buttons()
        buttons(bot, m).menu_buttons()
    elif m.text == 'Мои заказы 📋':
        bot.send_message(m.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, m).zakazy_search()
    elif m.text == 'Корзина 🗑️':
        bot.send_message(m.chat.id, f'Секунду..')
        poisk_tovar_in_base(bot, m).basket_search()
    elif m.text == 'О нас ⁉️':
        bot.send_message(m.chat.id, 'фрагмент в разработке')
    elif m.text == 'Контакты ☎️':
        bot.send_message(m.chat.id, 'фрагмент в разработке')


@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback(callback):
    global tovar_name, quantity, file, article, back_value
    wb = load_workbook('CCM.xlsx')
    ws = wb['МЛ Остатки штаб']
    list_one = []
    if callback.data == 'Да, хочу!':
        val = bot.send_message(callback.message.chat.id,
                               'Пожалуйста отправьте количество желаемого товара ЧИСЛОМ с помощью клавиатуры')
        bot.register_next_step_handler(val, amount)  # функция оформления заявки. Отправляет админу специальное сообщение о заявке
    elif callback.data == 'Не оплачено':
        bot.send_message(callback.message.chat.id,
                         f'Заявка оформлена и передана менеджеру, с Вами свяжутся в ближайшее время. '
                         'Спасибо, что выбрали нас.🤝\n'
                         f'Чтобы продолжить покупки выберите "Категории товаров 🗂️"')
        bot.send_message(admin_id, f'🚨!!!ВНИМАНИЕ!!!🚨\n'
                                   f'Поступила ЗАЯВКА от:\n'
                                   f'id чата: {callback.message.chat.id}\n'
                                   f'Имя: {callback.from_user.first_name}\n'
                                   f'Фамилия: {callback.from_user.last_name}\n'
                                   f'Ссылка: @{callback.from_user.username}\n'
                                   f'Товар: {tovar_name.tovar}\n'
                                   f'Количество: {quantity.quantity}\n'
                                   f'Оплата: Не оплачено')
        #poisk_tovar_in_base(bot, callback, article, tovar_name.tovar, quantity.quantity).zayavka_v_baze()
    elif callback.data == 'Оплачено':
        platezhy(bot, callback, article=article, tovar_name=tovar_name.tovar, quantity=quantity.quantity).chec_control()
    elif callback.data[:10] == 'delete_row':
        bot.send_message(callback.message.chat.id, f'Подчищаем базу..')
        poisk_tovar_in_base(bot, callback).basket_delete(callback.data[10:])
    elif callback.data == "Вернуться в начало":
        for row in ws.iter_rows(min_row=2, min_col=9, max_col=9, values_only=True):
            if row == (None,):
                break
            list_one.append(*row)
        list_one = list(set(list_one))
        file_open = open("menu_logo.jpeg", 'rb')
        buttons(bot, callback.message, kategoriya='раздел', list_one=list_one,
                image=file_open).razdely_buttons()

    elif len(list_one) == 0:
        back_value = "Вернуться в начало"
        list_two = []
        list_three = []
        kategoriya = None
        for row in ws.iter_rows(min_row=2, min_col=1, max_col=14, values_only=True):
            if row == (None,):
                break
            elif row[8] == callback.data:
                list_one.append(row[1][0:30])
                list_one = list(set(list_one))
                kategoriya = 'категорию'
            elif callback.data in str(row[1]):
                if len(row[2]) <= 25:
                    list_two.append((str(row[2])+'-'+str(row[3]), row[0]))
                    back_value = row[8]
                else:
                    list_two.append((f'{row[2][:15]}...{str((row[2])+str(row[3]))[-12:]}', row[0]))
                    back_value = row[8]
                kategoriya = 'товар'
            elif str(row[0]) == str(callback.data):
                tovar_name = row[2]
                article = row[0]
                image = row[10]
                size = row[3]
                price = row[4]
                vnalichii = row[7]
                your_price = row[5]
                size_web = row[13]
                bot.send_message(callback.message.chat.id, 'Секунду..')
                poisk_tovar_in_base(bot, callback.message, article, vnalichii=vnalichii, tovar_name=tovar_name,
                                    image=image, size=size, price=price,
                                    your_price=your_price, size_web=size_web).poisk_ostatok(back_value=row[1])
                list_three.append((row[0], row[10]))
        if len(list_one) != 0:
            file_open = open("menu_logo.jpeg", 'rb')
            list_one.append('Вернуться в начало')
            buttons(bot, callback.message, kategoriya=kategoriya, list_one=list_one,
                    image=file_open).razdely_buttons()
        elif len(list_two) != 0:
            file_open = open("menu_logo.jpeg", 'rb')
            list_two.append(('Вернуться назад', back_value))
            buttons(bot, callback.message, kategoriya=kategoriya, list_one=list_two,
                    image=file_open).marks_buttons()


def amount(message):  # функция регистрации заявки авто, которое отсутствует в каталоге бота
    wb = load_workbook('CCM.xlsx')
    ws = wb['кэш']
    try:
        int(message.text)
        for i in range(1, ws.max_row + 1):
            if str(ws.cell(i, 1).value) == str(message.chat.id):
                if int(message.text) <= int(ws.cell(i, 7).value) and int(message.text) != 0:
                    if ws.cell(i, 8).value is not None:
                        ws.cell(i, 6).value = message.text
                        wb.save('CCM.xlsx')
                        zayavka_done(bot=bot, message=message, number=ws.cell(i, 8).value)
                        break
                    else:
                        ws.cell(i, 6).value = message.text
                        wb.save('CCM.xlsx')
                        kb4 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
                        but1 = types.KeyboardButton(text='Вернуться в начало')
                        kb4.add(but1)
                        mes_num = bot.send_message(message.chat.id, 'Пожалуйста введите номер телефона',
                                                   reply_markup=kb4)
                        bot.register_next_step_handler(mes_num, save_number)
                        break
                else:
                    bot.send_message(message.chat.id,
                                     f'Увы, но указанное количество либо превышает остатки товара, либо равно 0. Отправьте '
                                     f'корректное значение.\n'
                                     f'Чтобы изменить товар выберите "Категории товаров 🗂️"')
                    buttons(bot, message).zayavka_buttons()
                    break
    except ValueError:
        bot.send_message(message.chat.id, f'Пожалуйста, укажите количество ЧИСЛОМ')
        buttons(bot, message).zayavka_buttons()


def save_number(message):
    number = message.text
    if number == "Вернуться в начало":
        chek_message_category(message)
    elif len(str(number)) >= 10 and ('+' in (str(number)) or '7' in (str(number)) or '8' in (str(number))):
        zayavka_done(bot=bot, message=message, number=number)
    else:
        bot.send_message(message.chat.id, 'указан некорректный номер.')
        kb4 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        but1 = types.KeyboardButton(text='Вернуться в начало')
        kb4.add(but1)
        mes_num = bot.send_message(message.chat.id, 'Пожалуйста введите номер телефона', reply_markup=kb4)
        bot.register_next_step_handler(mes_num, save_number)


def sent_message_perehvat_1(message):
    try:
        global rasylka
        rasylka = rasylka_message(message.text)  # хз почему message.id а не message.text но bot.copy_message() работает только так
        sent = bot.send_message(admin_id, 'Введите текст сообщения')
        bot.register_next_step_handler(sent, sent_message_perehvat_2)
    except ValueError:
        bot.send_message(admin_id, 'Неккоректное значение. Воспользуйтесь командой /sent_message еще раз')


def sent_message_perehvat_2(message):
    kb2 = types.ReplyKeyboardRemove()
    global rasylka
    bot.copy_message(rasylka.post, admin_id, message.id, reply_markup=kb2)
    bot.send_message(admin_id, 'Сообщение отправлено!')


bot.infinity_polling()
