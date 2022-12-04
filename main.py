# библиотека телеграм-бота
import telebot
# с помощью типов можно создавать клавиатуры
from telebot import types
# библиотека для выполнения фоновых процессов в определенное время
#from apscheduler.schedulers.background import BackgroundScheduler
# импорт из файла functions
import json
from functions import buttons, zayavka_done, poisk_tovar_in_base, tovar, Quantity, rasylka_message, admin_id, file
from passwords import *
article = None

token = code_mashine
bot = telebot.TeleBot(token)

tovar_name = None
quantity = None
rassylka = None


@bot.message_handler(commands=['start'])    # перехватчик команды /start
def start(message):
    file_open = open("start_logo.png", 'rb')    # открытие и чтение файла стартовой картинки
    bot.send_photo(message.chat.id, file_open, '''Здравствуйте!
Вас приветствует CCM_bot - Я помогу подобрать профессиональный хоккейный инвентарь по лучшим ценам. 🏆🏒🥇

Выберите "Категории товаров 🗂️" - для просмотра ассортимента по категориям
/help - все возможности бота''')
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
    global file
    if m.text == 'Категории товаров 🗂️' or m.text == "Вернуться в начало":
        buttons(bot, m, file=file, key='general_menu', kategoriya='категорию',
        image='https://drive.google.com/file/d/1m00gJSNw3vY6BB-3G-TA_Ec3b_Us2iZ3/view?usp=sharing').marks_buttons()
        buttons(bot, m).menu_buttons()
    if m.text == 'Заказы 📋':
        bot.send_message(m.chat.id, 'фрагмент в разработке')
    if m.text == 'Корзина 🗑️':
        bot.send_message(m.chat.id, 'фрагмент в разработке')
    if m.text == 'Вопросы-ответы ⁉️':
        bot.send_message(m.chat.id, 'фрагмент в разработке')
    if m.text == 'Контакты ☎️':
        bot.send_message(m.chat.id, 'фрагмент в разработке')


@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback(callback):
    global tovar_name, quantity, file, article
    if callback.data == "Вернуться в начало":
        buttons(bot, callback.message, file=file, key='general_menu', kategoriya='категорию',
                image='https://drive.google.com/file/d/1m00gJSNw3vY6BB-3G-TA_Ec3b_Us2iZ3/view?usp=sharing').marks_buttons()
    elif callback.data == "Вернуться в категорию 'Клюшки'":
        buttons(bot, callback.message, key='Kлюшки', kategoriya='подкатегорию',
                image='https://drive.google.com/file/d/1azEULeTNaBigbN5LXEBC3C4c-_PXFAHz/view?usp=share_link').marks_buttons()
    elif callback.data == 'Другое':
        buttons(bot, callback.message, key='Другое', kategoriya='подкатегорию').marks_buttons()
    elif callback.data == 'Да, хочу!':
        val = bot.send_message(callback.message.chat.id,
                               'Пожалуйста отправьте количество желаемого товара ЧИСЛОМ с помощью клавиатуры')
        bot.register_next_step_handler(val, amount)  # функция оформления заявки. Отправляет админу специальное сообщение о заявке
    elif callback.data == 'Коньки':
        buttons(bot, callback.message, file=file['general_menu'], key='Коньки', kategoriya='подкатегорию',
                image='https://drive.google.com/file/d/1FZc0LZQr5BzN_0ZUDgtPFmILhXlRtwE2/view?usp=share_link').marks_buttons()
    elif callback.data == 'Клюшки':
        buttons(bot, callback.message, file=file['general_menu'], key='Клюшки', kategoriya='подкатегорию',
                image='https://drive.google.com/file/d/1azEULeTNaBigbN5LXEBC3C4c-_PXFAHz/view?usp=share_link').marks_buttons()
    elif callback.data == 'Защита':
        buttons(bot, callback.message, file=file['general_menu'], key='Защита', kategoriya='подкатегорию',
                image='https://drive.google.com/file/d/1UYHhznQxW19HywsxNgrKBFNO4BH5-TnH/view?usp=share_link').marks_buttons()
    elif callback.data == 'Бенди':
        buttons(bot, callback.message, file=file['general_menu'], key='Бенди', kategoriya='товар',
                image='https://drive.google.com/file/d/1Q-mrh_MN2VzxNgfrD03XuhAMGzmwttp7/view?usp=share_link').marks_buttons()
    elif callback.data == 'Одежда':
        buttons(bot, callback.message, file=file['general_menu'], key='Одежда', kategoriya='подкатегорию',
                image='https://drive.google.com/file/d/16IXw_RBWXsCv-aW6OsHEsbfi2ru4IRh3/view?usp=share_link').marks_buttons()
    elif callback.data == 'Игровая форма':
        buttons(bot, callback.message, file=file['general_menu'], key='Игровая форма', kategoriya='подкатегорию',
                image='https://drive.google.com/file/d/1hop7DZetV0qCjrWWU9xTLgBcoCLz9lUu/view?usp=share_link').marks_buttons()
    elif callback.data == 'Аксессуары':
        buttons(bot, callback.message, file=file['general_menu'], key='Аксессуары', kategoriya='подкатегорию',
                image='https://drive.google.com/file/d/19kwKVYj1lt4lMqLjeeWdLyPOgX0YnD9_/view?usp=share_link').marks_buttons()
    elif callback.data == 'Ворота':
        buttons(bot, callback.message, file=file['general_menu'], key='Ворота', kategoriya='товар',
                image='https://drive.google.com/file/d/13C6xMvyCTyawCSoJzL44yIfmB0UpVqzm/view?usp=share_link').marks_buttons()
    elif callback.data == 'Детские наборы':
        buttons(bot, callback.message, file=file['general_menu'], key='Детские наборы', kategoriya='товар',
                image='https://drive.google.com/file/d/1UA2xpltfxbI0UM27onRjGrnkYYPrTVzw/view?usp=share_link').marks_buttons()
    elif callback.data == 'Кроссовки':
        buttons(bot, callback.message, file=file['general_menu'], key='Кроссовки', kategoriya='товар').marks_buttons()
    elif callback.data == 'Перчатки':
        buttons(bot, callback.message, file=file['general_menu'], key='Перчатки', kategoriya='товар').marks_buttons()
    elif callback.data == 'Ролики':
        buttons(bot, callback.message, file=file['general_menu'], key='Ролики', kategoriya='товар').marks_buttons()
    elif callback.data == 'Судейская форма':
        buttons(bot, callback.message, file=file['general_menu'], key='Судейская форма', kategoriya='товар').marks_buttons()
    elif callback.data == 'Термобельё':
        buttons(bot, callback.message, file=file['general_menu'], key='Термобельё', kategoriya='товар').marks_buttons()
    elif callback.data == 'Услуги':
        buttons(bot, callback.message, file=file['general_menu'], key='Услуги', kategoriya='товар').marks_buttons()
    elif callback.data == 'Шапки/кепки':
        buttons(bot, callback.message, file=file['general_menu'], key='Шапки/кепки', kategoriya='товар').marks_buttons()
    elif callback.data == 'Шлемы':
        buttons(bot, callback.message, file=file['general_menu'], key='Шлемы', kategoriya='товар').marks_buttons()
    elif callback.data == 'Аксессуары для клюшек':
        buttons(bot, callback.message, file=file['general_menu'], key='Аксессуары для клюшек',
                kategoriya='товар').marks_buttons()
    elif callback.data == 'Аксессуары для коньков':
        buttons(bot, callback.message, file=file['general_menu'], key='Аксессуары для коньков',
                kategoriya='товар').marks_buttons()
    elif callback.data == 'Аксессуары для шлемов':
        buttons(bot, callback.message, file=file['general_menu'], key='Аксессуары для шлемов', kategoriya='товар').marks_buttons()
    elif callback.data == 'Ворота SH MINI STEEL 3x2 Bauer Street Brana':
        tovar_name = tovar(callback.data)
        article = (file['general_menu']['Ворота']['Ворота SH MINI STEEL 3x2 Bauer Street Brana'])[0]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar).poisk_ostatok()
    elif callback.data == 'Красная лента (N SZ)':
        tovar_name = tovar(callback.data)
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, tovar_name.tovar).poisk_ostatok()
    elif callback.data == 'Черная лента (L)':
        tovar_name = tovar(callback.data)
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, tovar_name.tovar).poisk_ostatok()
    elif callback.data == 'Черная лента (N SZ)':
        tovar_name = tovar(callback.data)
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, tovar_name.tovar).poisk_ostatok()


#def drugoe(message):  # функция регистрации заявки авто, которое отсутствует в каталоге бота
 #   global tovar_name
  #  tovar_name = tovar(message.text)   # модели присваивается название введенное клиентов в сообщении
   # bot.send_message(message.chat.id, 'Cпасибо! Я передал информацию менеджеру. Ответ поступит Вам в ближайшее '
   #                                   'время.')
   # bot.send_message('1338281106', f'🚨!!!СРОЧНО!!!🚨\n'
    #                               f'Хозяин, поступил запрос на отсутствующий товар от:\n'
     #                              f'Имя: {message.from_user.first_name}\n'
      #                             f'Фамилия: {message.from_user.last_name}\n'
       #                            f'Никнейм: {message.from_user.username}\n'
        #                           f'Ссылка: @{message.from_user.username}\n'
         #                          f'Авто: {tovar_name}\n')
    #clients_base(bot, message, tovar).chec_and_record()  # класс проверки клиента в базе и его запись в базу
                                                              # в случае отсутствия
def amount(message):  # функция регистрации заявки авто, которое отсутствует в каталоге бота
    global quantity, article
    quantity = Quantity(message.text)
    zayavka_done(bot=bot, message=message, article=article, tovar_name=tovar_name.tovar, quantity=quantity.quantity)


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


