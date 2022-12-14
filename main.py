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

token = lemonade
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
    if m.text == 'Категории товаров 🗂️':
        buttons(bot, m, file=file, key='general_menu', kategoriya='категорию',
        image='https://drive.google.com/file/d/1m00gJSNw3vY6BB-3G-TA_Ec3b_Us2iZ3/view?usp=sharing').marks_buttons()
    elif m.text == "Вернуться в начало":
        buttons(bot, m, file=file, key='general_menu', kategoriya='категорию',
        image='https://drive.google.com/file/d/1m00gJSNw3vY6BB-3G-TA_Ec3b_Us2iZ3/view?usp=sharing').marks_buttons()
        buttons(bot, m).menu_buttons()
    elif m.text == 'История заказов 📋':
        bot.send_message(m.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, m).zakazy_search()
    elif m.text == 'Корзина 🗑️':
        bot.send_message(m.chat.id, f'Секунду..')
        poisk_tovar_in_base(bot, m).basket_search()
    elif m.text == 'Вопросы-ответы ⁉️':
        bot.send_message(m.chat.id, 'фрагмент в разработке')
    elif m.text == 'Контакты ☎️':
        bot.send_message(m.chat.id, 'фрагмент в разработке')


@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback(callback):
    global tovar_name, quantity, file, article
    if callback.data == 'Да, хочу!' or callback.data == 'Онлайн оплата':
        val = bot.send_message(callback.message.chat.id,
                               'Пожалуйста отправьте количество желаемого товара ЧИСЛОМ с помощью клавиатуры')
        bot.register_next_step_handler(val, amount)  # функция оформления заявки. Отправляет админу специальное сообщение о заявке
    elif callback.data[:10] == 'delete_row':
        bot.send_message(callback.message.chat.id, f'Подчищаем базу..')
        poisk_tovar_in_base(bot, callback.message).basket_delete(callback.data[10:])
    elif callback.data == "Вернуться в начало":
        buttons(bot, callback.message, file=file, key='general_menu', kategoriya='категорию',
                image='https://drive.google.com/file/d/1m00gJSNw3vY6BB-3G-TA_Ec3b_Us2iZ3/view?usp=sharing').marks_buttons()
    elif callback.data == "Назад в категорию 'Защита'":
        buttons(bot, callback.message, file=file['general_menu'], key='Защита', kategoriya='подкатегорию',
                image='https://drive.google.com/file/d/1nG0RvJ9L6Ez_O9SOjllhFn2OvszB92TE/view?usp=share_link').marks_buttons()
    elif callback.data == "Назад в категорию 'Детские наборы'":
        buttons(bot, callback.message, file=file['general_menu'], key='Детские наборы', kategoriya='подкатегорию',
                image='https://ccm.ru/upload/iblock/c87/cs1395t51nkhc535xwgsnt7xz54upeoi/STARTER-KIT-YT-2.jpg').marks_buttons()
    elif callback.data == "Назад в подкатегорию 'Нагрудники'":
        buttons(bot, callback.message, file=file['general_menu']['Защита'], key='Нагрудники', kategoriya='подкатегорию',
                image='https://drive.google.com/file/d/1UYHhznQxW19HywsxNgrKBFNO4BH5-TnH/view?usp=share_link').marks_buttons()
    elif callback.data == "Назад в подкатегорию 'Налокотники'":
        buttons(bot, callback.message, file=file['general_menu']['Защита'], key='Налокотники', kategoriya='подкатегорию',
                image='https://ccm.ru/upload/iblock/917/o7zoblszps82kks580grj9qaijern4gm/EP-AS580-01.jpg').marks_buttons()
    elif callback.data == "Назад в подкатегорию 'Трусы'":
        buttons(bot, callback.message, file=file['general_menu']['Защита'], key='Трусы', kategoriya='подкатегорию',
                image='https://ccm.ru/upload/iblock/dcc/hp230.jpg').marks_buttons()
    elif callback.data == "Назад в подкатегорию 'Щитки'":
        buttons(bot, callback.message, file=file['general_menu']['Защита'], key='Щитки', kategoriya='подкатегорию',
                image='https://ccm.ru/upload/iblock/4af/5e58qkwxwmbr0rqy6eizqxcnstq4dd0b/SG-AS580-JR-01.jpg').marks_buttons()
    elif callback.data == "Назад в категорию 'Аксессуары'":
        buttons(bot, callback.message, file=file['general_menu'], key='Аксессуары', kategoriya='подкатегорию',
                image='https://ccm.ru/upload/iblock/4af/5e58qkwxwmbr0rqy6eizqxcnstq4dd0b/SG-AS580-JR-01.jpg').marks_buttons()

    elif callback.data in file['general_menu']:
        buttons(bot, callback.message, file=file['general_menu'], key=callback.data, kategoriya='подкатегорию',
              image='https://drive.google.com/file/d/1nG0RvJ9L6Ez_O9SOjllhFn2OvszB92TE/view?usp=share_'
                    'link').marks_buttons()
    elif callback.data in file['general_menu']['Защита']:
        buttons(bot, callback.message, file=file['general_menu']['Защита'], key=callback.data,
        kategoriya='товар', image='https://drive.google.com/file/d/1UYHhznQxW19HywsxNgrKBFNO4BH5-TnH/view?usp=share_'
                                  'link').marks_buttons()
    elif callback.data in file['general_menu']['Аксессуары']:
        try:
            buttons(bot, callback.message, file=file['general_menu']['Аксессуары'], key=callback.data,
                    kategoriya='товар', image='https://drive.google.com/file/d/19kwKVYj1lt4lMqLjeeWdLyPOgX0YnD9_/view?'
                                              'usp=share_link').marks_buttons()
        except AttributeError:
            tovar_name = tovar(callback.data)
            source = (file['general_menu']['Аксессуары'][callback.data])
            article = source[0]
            image = source[1]
            opisanie = source[2]
            price = source[3]
            bot.send_message(callback.message.chat.id, 'Секунду..')
            poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                                price=price).poisk_ostatok(back_value="Назад в категорию 'Аксессуары'")

    elif callback.data in file['general_menu']['Защита']['Нагрудники']:
        try:
            buttons(bot, callback.message, file=file['general_menu']['Защита']['Нагрудники'], key=callback.data,
                    kategoriya='товар', image='https://drive.google.com/file/d/1UYHhznQxW19HywsxNgrKBFNO4BH5-TnH/view?'
                                              'usp=share_link').marks_buttons()
        except AttributeError:
            tovar_name = tovar(callback.data)
            source = (file['general_menu']['Защита']['Нагрудники'][callback.data])
            article = source[0]
            image = source[1]
            opisanie = source[2]
            price = source[3]
            bot.send_message(callback.message.chat.id, 'Секунду..')
            poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                                price=price).poisk_ostatok(back_value="Назад в подкатегорию 'Нагрудники'")

    elif callback.data in file['general_menu']['Ворота']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Ворота'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok()
    elif callback.data in file['general_menu']['Бенди']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Бенди'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok()
    elif callback.data in file['general_menu']['Детские наборы']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Детские наборы'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в категорию 'Детские наборы'")

    elif callback.data in file['general_menu']['Защита']['Нагрудники']['350']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Защита']['Нагрудники']['350'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в подкатегорию 'Нагрудники'")
    elif callback.data in file['general_menu']['Защита']['Нагрудники']['9060']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Защита']['Нагрудники']['9060'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в подкатегорию 'Нагрудники'")
    elif callback.data in file['general_menu']['Защита']['Нагрудники']['9040']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Защита']['Нагрудники']['9040'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в подкатегорию 'Нагрудники'")
    elif callback.data in file['general_menu']['Защита']['Нагрудники']['9080']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Защита']['Нагрудники']['9080'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в подкатегорию 'Нагрудники'")
    elif callback.data in file['general_menu']['Защита']['Нагрудники']['9550']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Защита']['Нагрудники']['9550'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в подкатегорию 'Нагрудники'")
    elif callback.data in file['general_menu']['Защита']['Нагрудники']['AS1']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Защита']['Нагрудники']['AS1'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в подкатегорию 'Нагрудники'")
    elif callback.data in file['general_menu']['Защита']['Нагрудники']['BAUER']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Защита']['Нагрудники']['BAUER'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в подкатегорию 'Нагрудники'")
    elif callback.data in file['general_menu']['Защита']['Нагрудники']['FT1']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Защита']['Нагрудники']['FT1'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в подкатегорию 'Нагрудники'")
    elif callback.data in file['general_menu']['Защита']['Нагрудники']['SP FT485']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Защита']['Нагрудники']['SP FT485'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в подкатегорию 'Нагрудники'")

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


