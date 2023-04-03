# библиотека телеграм-бота
import telebot
# с помощью типов можно создавать клавиатуры
from telebot import types
# библиотека для выполнения фоновых процессов в определенное время
#from apscheduler.schedulers.background import BackgroundScheduler
# импорт из файла functions
import json
from functions import buttons, zayavka_done, poisk_tovar_in_base, tovar, Quantity, rasylka_message, admin_id, file, \
    platezhy
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
    if m.text == 'Каталог 🗂️':
        buttons(bot, m, file=file, key='general_menu', kategoriya='категорию',
        image='https://drive.google.com/file/d/1m00gJSNw3vY6BB-3G-TA_Ec3b_Us2iZ3/view?usp=sharing').marks_buttons()
    elif m.text == "Вернуться в начало":
        buttons(bot, m, file=file, key='general_menu', kategoriya='категорию',
        image='https://drive.google.com/file/d/1m00gJSNw3vY6BB-3G-TA_Ec3b_Us2iZ3/view?usp=sharing').marks_buttons()
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
    global tovar_name, quantity, file, article
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
        poisk_tovar_in_base(bot, callback, article, tovar_name.tovar, quantity.quantity).zayavka_v_baze()
    elif callback.data == 'Оплачено':
        platezhy(bot, callback, article=article, tovar_name=tovar_name.tovar, quantity=quantity.quantity).chec_control()
    elif callback.data[:10] == 'delete_row':
        bot.send_message(callback.message.chat.id, f'Подчищаем базу..')
        poisk_tovar_in_base(bot, callback).basket_delete(callback.data[10:])
    elif callback.data == "Вернуться в начало":
        buttons(bot, callback.message, file=file, key='general_menu', kategoriya='категорию',
                image='https://drive.google.com/file/d/1m00gJSNw3vY6BB-3G-TA_Ec3b_Us2iZ3/view?usp=sharing').marks_buttons()
    elif callback.data == "Назад в категорию 'Защита'":
        buttons(bot, callback.message, file=file['general_menu'], key='Защита', kategoriya='подкатегорию',
                image='https://drive.google.com/file/d/1nG0RvJ9L6Ez_O9SOjllhFn2OvszB92TE/view?usp=share_link').marks_buttons()
    elif callback.data == "Назад в категорию 'Детские наборы'":
        buttons(bot, callback.message, file=file['general_menu'], key='Детские наборы', kategoriya='подкатегорию',
                image='https://ccm.ru/upload/iblock/c87/cs1395t51nkhc535xwgsnt7xz54upeoi/STARTER-KIT-YT-2.jpg').marks_buttons()
    elif callback.data == "Назад в категорию 'Аксессуары клю'":
        buttons(bot, callback.message, file=file['general_menu'], key='Аксессуары для клюшек', kategoriya='товар',
                image='https://sportlandia.md/kcfinder/upload/images/51/element-1.jpg').marks_buttons()
    elif callback.data == "Назад в категорию 'Аксессуары шле'":
        buttons(bot, callback.message, file=file['general_menu'], key='Аксессуары для шлемов', kategoriya='товар',
                image='https://hockey-shop.ru/upload/iblock/6dd/6dda90c129fc19250a5209f05dc8865a.jpg').marks_buttons()
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
    elif callback.data == "Назад в подкатегорию 'Носки'":
        buttons(bot, callback.message, file=file['general_menu']['Аксессуары'], key='Носки', kategoriya='подкатегорию',
                image='https://www.sportdepo.ru/upload/iblock/232/2323999d306929be60588acc7e3a7aab.jpeg').marks_buttons()
    elif callback.data == "Назад в категорию 'Аксессуары'":
        buttons(bot, callback.message, file=file['general_menu'], key='Аксессуары', kategoriya='подкатегорию',
                image='https://xtrick.ru/uploadedFiles/eshopimages/icons/250x200/1_194.jpg').marks_buttons()
    elif callback.data == "Назад в категорию 'Вратарская эки..'":
        buttons(bot, callback.message, file=file['general_menu'], key='Вратарская экипировка', kategoriya='подкатегорию',
                image='https://sportishka.com/uploads/posts/2022-11/thumbs/1667454848_31-sportishka-com-p-stoika-vratarya-v-khokkee-instagram-36.jpg').marks_buttons()
    elif callback.data == "Назад в категорию 'Клюшки'":
        buttons(bot, callback.message, file=file['general_menu'], key='Клюшки', kategoriya='подкатегорию',
                image='https://hock5.ru/image/cache/catalog/import_files/a6/a665b609-24cd-11eb-96fc-f46d04194956_46bc3b98-27df-11eb-96fc-f46d04194956-700x700.png').marks_buttons()
    elif callback.data == "Назад в категорию 'Кроссовки'":
        buttons(bot, callback.message, file=file['general_menu'], key='Кроссовки', kategoriya='товар',
                image='https://avatars.mds.yandex.net/get-mpic/6342941/img_id3400060433266196792.jpeg/orig').marks_buttons()
    elif callback.data == "Назад в категорию 'Коньки'":
        buttons(bot, callback.message, file=file['general_menu'], key='Коньки', kategoriya='подкатегорию',
                image='https://limpopo.kz/image/cache/catalog/produsts/CCM/2028148-2000x2000w.jpg').marks_buttons()
    elif callback.data == "Назад в категорию 'Ролики'":
        buttons(bot, callback.message, file=file['general_menu'], key='Ролики', kategoriya='товар',
                image='https://cdn.shoplightspeed.com/shops/608796/files/28620336/image.jpg').marks_buttons()
    elif callback.data == "Назад в категорию 'Перчатки'":
        buttons(bot, callback.message, file=file['general_menu'], key='Перчатки', kategoriya='подкатегорию',
                image='https://ccm.ru/upload/iblock/744/CCM-Jetspeed-FT4-Senior-Hockey-Gloves-NVWH.jpg').marks_buttons()

    elif callback.data in file['general_menu']:
        buttons(bot, callback.message, file=file['general_menu'], key=callback.data, kategoriya='подкатегорию',
              image='https://drive.google.com/file/d/1nG0RvJ9L6Ez_O9SOjllhFn2OvszB92TE/view?usp=share_'
                    'link').marks_buttons()
    elif callback.data in file['general_menu']['Защита']:
        buttons(bot, callback.message, file=file['general_menu']['Защита'], key=callback.data,
        kategoriya='товар', image='https://sportishka.com/uploads/posts/2021-12/1639710078_6-sportishka-com-p-'
                                  'ekipirovka-khokkeista-sport-krasvivo-foto-6.jpg').marks_buttons()
    elif callback.data in file['general_menu']['Аксессуары']:
        buttons(bot, callback.message, file=file['general_menu']['Аксессуары'], key=callback.data,
                kategoriya='товар', image='https://xtrick.ru/uploadedFiles/eshopimages/icons/250x200/1_194.jpg').marks_buttons()
    elif callback.data in file['general_menu']['Вратарская экипировка']:
        try:
            buttons(bot, callback.message, file=file['general_menu']['Вратарская экипировка'], key=callback.data,
                    kategoriya='товар', image='https://sportishka.com/uploads/posts/2022-11/thumbs/1667454848_31-sportishka-com-p-stoika-vratarya-v-khokkee-instagram-36.jpg?'
                                              'usp=share_link').marks_buttons()
        except AttributeError:
            tovar_name = tovar(callback.data)
            source = (file['general_menu']['Вратарская экипировка'][callback.data])
            article = source[0]
            image = source[1]
            opisanie = source[2]
            price = source[3]
            bot.send_message(callback.message.chat.id, 'Секунду..')
            poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                                price=price).poisk_ostatok(back_value="Назад в категорию 'Вратарская эки..'")
    elif callback.data in file['general_menu']['Клюшки']:
        buttons(bot, callback.message, file=file['general_menu']['Клюшки'], key=callback.data,
        kategoriya='подкатегорию', image='https://hock5.ru/image/cache/catalog/import_files/a6/a665b609-24cd-11eb-96'
                                         'fc-f46d04194956_46bc3b98-27df-11eb-96fc-f46d04194956-700x700.png').marks_buttons()
    elif callback.data in file['general_menu']['Коньки']:
        buttons(bot, callback.message, file=file['general_menu']['Коньки'], key=callback.data,
        kategoriya='товар', image='https://limpopo.kz/image/cache/catalog/produsts/CCM/2028148-'
                                         '2000x2000w.jpg').marks_buttons()
    elif callback.data in file['general_menu']['Перчатки']:
        buttons(bot, callback.message, file=file['general_menu']['Перчатки'], key=callback.data,
        kategoriya='товар', image='https://ccm.ru/upload/iblock/744/CCM-Jetspeed-FT4-Senior-Hockey-Gloves-'
                                  'NVWH.jpg').marks_buttons()

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
    elif callback.data in file['general_menu']['Защита']['Налокотники']:
        try:
            buttons(bot, callback.message, file=file['general_menu']['Защита']['Налокотники'], key=callback.data,
                    kategoriya='товар', image='https://ccm.ru/upload/iblock/9a5/f7nbtw8nw0oepiwvm08mn0sguimof09j/'
                                              'EP-AS5-PRO-01.jpg').marks_buttons()
        except AttributeError:
            tovar_name = tovar(callback.data)
            source = (file['general_menu']['Защита']['Налокотники'][callback.data])
            article = source[0]
            image = source[1]
            opisanie = source[2]
            price = source[3]
            bot.send_message(callback.message.chat.id, 'Секунду..')
            poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                                price=price).poisk_ostatok(back_value="Назад в подкатегорию 'Налокотники'")
    elif callback.data in file['general_menu']['Защита']['Трусы']:
        try:
            buttons(bot, callback.message, file=file['general_menu']['Защита']['Трусы'], key=callback.data,
                    kategoriya='товар', image='https://ccm.ru/upload/iblock/dcc/hp230.jpg').marks_buttons()
        except AttributeError:
            tovar_name = tovar(callback.data)
            source = (file['general_menu']['Защита']['Трусы'][callback.data])
            article = source[0]
            image = source[1]
            opisanie = source[2]
            price = source[3]
            bot.send_message(callback.message.chat.id, 'Секунду..')
            poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                                price=price).poisk_ostatok(back_value="Назад в подкатегорию 'Трусы'")
    elif callback.data in file['general_menu']['Защита']['Щитки']:
        try:
            buttons(bot, callback.message, file=file['general_menu']['Защита']['Щитки'], key=callback.data,
                    kategoriya='товар', image='https://ccm.ru/upload/resize_cache/iblock/b2b/07gwmr1dtb9batbhcztjo3a40ci7s3f1/252_290_1/SG-AS580-JR-01.jpg').marks_buttons()
        except AttributeError:
            tovar_name = tovar(callback.data)
            source = (file['general_menu']['Защита']['Щитки'][callback.data])
            article = source[0]
            image = source[1]
            opisanie = source[2]
            price = source[3]
            bot.send_message(callback.message.chat.id, 'Секунду..')
            poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                                price=price).poisk_ostatok(back_value="Назад в подкатегорию 'Щитки'")

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
    elif callback.data in file['general_menu']['Аксессуары для клюшек']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Аксессуары для клюшек'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в категорию 'Аксессуары клю'")
    elif callback.data in file['general_menu']['Аксессуары для шлемов']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Аксессуары для шлемов'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в категорию 'Аксессуары шле'")
    elif callback.data in file['general_menu']['Кроссовки']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Кроссовки'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в категорию 'Кроссовки'")
    elif callback.data in file['general_menu']['Ролики']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Ролики'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в категорию 'Ролики'")

    elif callback.data in file['general_menu']['Защита']['Нагрудники']['(350) Нагрудники']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Защита']['Нагрудники']['(350) Нагрудники'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в подкатегорию 'Нагрудники'")
    elif callback.data in file['general_menu']['Защита']['Нагрудники']['(9060) Нагрудники']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Защита']['Нагрудники']['(9060) Нагрудники'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в подкатегорию 'Нагрудники'")
    elif callback.data in file['general_menu']['Защита']['Нагрудники']['(9040) Нагрудники']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Защита']['Нагрудники']['(9040) Нагрудники'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в подкатегорию 'Нагрудники'")
    elif callback.data in file['general_menu']['Защита']['Нагрудники']['(9080) Нагрудники']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Защита']['Нагрудники']['(9080) Нагрудники'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в подкатегорию 'Нагрудники'")
    elif callback.data in file['general_menu']['Защита']['Нагрудники']['(9550) Нагрудники']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Защита']['Нагрудники']['(9550) Нагрудники'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в подкатегорию 'Нагрудники'")
    elif callback.data in file['general_menu']['Защита']['Нагрудники']['(AS1) Нагрудники']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Защита']['Нагрудники']['(AS1) Нагрудники'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в подкатегорию 'Нагрудники'")
    elif callback.data in file['general_menu']['Защита']['Нагрудники']['(BAUER) Нагрудники']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Защита']['Нагрудники']['(BAUER) Нагрудники'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в подкатегорию 'Нагрудники'")
    elif callback.data in file['general_menu']['Защита']['Нагрудники']['(FT1) Нагрудники']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Защита']['Нагрудники']['(FT1) Нагрудники'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в подкатегорию 'Нагрудники'")
    elif callback.data in file['general_menu']['Защита']['Нагрудники']['(SP FT485) Нагрудники']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Защита']['Нагрудники']['(SP FT485) Нагрудники'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в подкатегорию 'Нагрудники'")

    elif callback.data in file['general_menu']['Защита']['Налокотники']['(350) Налокотники']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Защита']['Налокотники']['(350) Налокотники'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в подкатегорию 'Налокотники'")
    elif callback.data in file['general_menu']['Защита']['Налокотники']['(9040) Налокотники']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Защита']['Налокотники']['(9040) Налокотники'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в подкатегорию 'Налокотники'")
    elif callback.data in file['general_menu']['Защита']['Налокотники']['(9060) Налокотники']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Защита']['Налокотники']['(9060) Налокотники'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в подкатегорию 'Налокотники'")
    elif callback.data in file['general_menu']['Защита']['Налокотники']['(9080) Налокотники']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Защита']['Налокотники']['(9080) Налокотники'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в подкатегорию 'Налокотники'")
    elif callback.data in file['general_menu']['Защита']['Налокотники']['(AS1) Налокотники']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Защита']['Налокотники']['(AS1) Налокотники'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в подкатегорию 'Налокотники'")
    elif callback.data in file['general_menu']['Защита']['Налокотники']['(BAUER) Налокотники']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Защита']['Налокотники']['(BAUER) Налокотники'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в подкатегорию 'Налокотники'")
    elif callback.data in file['general_menu']['Защита']['Налокотники']['(EP 9550) Налокотники']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Защита']['Налокотники']['(EP 9550) Налокотники'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в подкатегорию 'Налокотники'")
    elif callback.data in file['general_menu']['Защита']['Налокотники']['(EP FT485) Налокотники']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Защита']['Налокотники']['(EP FT485) Налокотники'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в подкатегорию 'Налокотники'")
    elif callback.data in file['general_menu']['Защита']['Налокотники']['(FT1) Налокотники']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Защита']['Налокотники']['(FT1) Налокотники'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в подкатегорию 'Налокотники'")

    elif callback.data in file['general_menu']['Защита']['Трусы']['(9040) Трусы']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Защита']['Трусы']['(9040) Трусы'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в подкатегорию 'Трусы'")
    elif callback.data in file['general_menu']['Защита']['Трусы']['(9060) Трусы']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Защита']['Трусы']['(9060) Трусы'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в подкатегорию 'Трусы'")
    elif callback.data in file['general_menu']['Защита']['Трусы']['(9080) Трусы']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Защита']['Трусы']['(9080) Трусы'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в подкатегорию 'Трусы'")
    elif callback.data in file['general_menu']['Защита']['Трусы']['(9550) Трусы']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Защита']['Трусы']['(9550) Трусы'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в подкатегорию 'Трусы'")
    elif callback.data in file['general_menu']['Защита']['Трусы']['(AS1) Трусы']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Защита']['Трусы']['(AS1) Трусы'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в подкатегорию 'Трусы'")
    elif callback.data in file['general_menu']['Защита']['Трусы']['(BAUER) Трусы']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Защита']['Трусы']['(BAUER) Трусы'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в подкатегорию 'Трусы'")
    elif callback.data in file['general_menu']['Защита']['Трусы']['(FT350) Трусы']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Защита']['Трусы']['(FT350) Трусы'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в подкатегорию 'Трусы'")
    elif callback.data in file['general_menu']['Защита']['Трусы']['(FT370) Трусы']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Защита']['Трусы']['(FT370) Трусы'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в подкатегорию 'Трусы'")
    elif callback.data in file['general_menu']['Защита']['Трусы']['(HP 485) Трусы']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Защита']['Трусы']['(HP 485) Трусы'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в подкатегорию 'Трусы'")
    elif callback.data in file['general_menu']['Защита']['Трусы']['(HP FT4) Трусы']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Защита']['Трусы']['(HP FT4) Трусы'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в подкатегорию 'Трусы'")
    elif callback.data in file['general_menu']['Защита']['Трусы']['(HP FT4 PRO) Трусы']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Защита']['Трусы']['(HP FT4 PRO) Трусы'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в подкатегорию 'Трусы'")

    elif callback.data in file['general_menu']['Защита']['Щитки']['(9550) Щитки']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Защита']['Щитки']['(9550) Щитки'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в подкатегорию 'Щитки'")
    elif callback.data in file['general_menu']['Защита']['Щитки']['(BAUER) Щитки']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Защита']['Щитки']['(BAUER) Щитки'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в подкатегорию 'Щитки'")
    elif callback.data in file['general_menu']['Защита']['Щитки']['(SG 9040) Щитки']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Защита']['Щитки']['(SG 9040) Щитки'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в подкатегорию 'Щитки'")
    elif callback.data in file['general_menu']['Защита']['Щитки']['(SG 9080) Щитки']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Защита']['Щитки']['(SG 9080) Щитки'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в подкатегорию 'Щитки'")
    elif callback.data in file['general_menu']['Защита']['Щитки']['(SG FT485) Щитки']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Защита']['Щитки']['(SG FT485) Щитки'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в подкатегорию 'Щитки'")

    elif callback.data in file['general_menu']['Вратарская экипировка']['Вратарские блины']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Вратарская экипировка']['Вратарские блины'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в категорию 'Вратарская эки..'")
    elif callback.data in file['general_menu']['Вратарская экипировка']['Вратарские панцыри-нагрудники']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Вратарская экипировка']['Вратарские панцыри-нагрудники'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в категорию 'Вратарская эки..'")
    elif callback.data in file['general_menu']['Вратарская экипировка']['Вратарские шлемы']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Вратарская экипировка']['Вратарские шлемы'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в категорию 'Вратарская эки..'")

    elif callback.data in file['general_menu']['Аксессуары']['Баул хоккейный']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Аксессуары']['Баул хоккейный'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в категорию 'Аксессуары'")
    elif callback.data in file['general_menu']['Аксессуары']['Бутылки']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Аксессуары']['Бутылки'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в категорию 'Аксессуары'")
    elif callback.data in file['general_menu']['Аксессуары']['Защита шеи']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Аксессуары']['Защита шеи'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в категорию 'Аксессуары'")
    elif callback.data in file['general_menu']['Аксессуары']['Капы']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Аксессуары']['Капы'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в категорию 'Аксессуары'")
    elif callback.data in file['general_menu']['Аксессуары']['Ленты']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Аксессуары']['Ленты'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в категорию 'Аксессуары'")
    elif callback.data in file['general_menu']['Аксессуары']['Подтяжки']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Аксессуары']['Подтяжки'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в категорию 'Аксессуары'")
    elif callback.data in file['general_menu']['Аксессуары']['Защита паха']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Аксессуары']['Защита паха'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в категорию 'Аксессуары'")
    elif callback.data in file['general_menu']['Аксессуары']['Сумки']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Аксессуары']['Сумки'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в категорию 'Аксессуары'")
    elif callback.data in file['general_menu']['Аксессуары']['Хоккейный свитер']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Аксессуары']['Хоккейный свитер'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в категорию 'Аксессуары'")
    elif callback.data in file['general_menu']['Аксессуары']['Другое']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Аксессуары']['Другое'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в категорию 'Аксессуары'")
    elif callback.data in file['general_menu']['Аксессуары']['Носки']:
        try:
            buttons(bot, callback.message, file=file['general_menu']['Аксессуары']['Носки'], key=callback.data,
                    kategoriya='товар', image='https://www.sportdepo.ru/upload/iblock/232/2323999d306929be60588acc7e3a7'
                                              'aab.jpeg').marks_buttons()
        except AttributeError:
            tovar_name = tovar(callback.data)
            source = (file['general_menu']['Аксессуары']['Носки'][callback.data])
            article = source[0]
            image = source[1]
            opisanie = source[2]
            price = source[3]
            bot.send_message(callback.message.chat.id, 'Секунду..')
            poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                                price=price).poisk_ostatok(back_value="Назад в подкатегорию 'Аксессуары'")
    elif callback.data in file['general_menu']['Аксессуары']['Носки']['Носки Bauer']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Аксессуары']['Носки']['Носки Bauer'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в подкатегорию 'Носки'")
    elif callback.data in file['general_menu']['Аксессуары']['Носки']['Носки CCM']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Аксессуары']['Носки']['Носки CCM'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в подкатегорию 'Носки'")
    elif callback.data in file['general_menu']['Аксессуары']['Носки']['Носки Kappa']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Аксессуары']['Носки']['Носки Kappa'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в подкатегорию 'Носки'")

    elif callback.data in file['general_menu']['Клюшки']['(AS4 PRO) Клюшки']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Клюшки']['(AS4 PRO) Клюшки'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в категорию 'Клюшки'")
    elif callback.data in file['general_menu']['Клюшки']['(BAUER) Клюшки']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Клюшки']['(BAUER) Клюшки'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в категорию 'Клюшки'")
    elif callback.data in file['general_menu']['Клюшки']['(HS FT5) Клюшки']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Клюшки']['(HS FT5) Клюшки'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в категорию 'Клюшки'")
    elif callback.data in file['general_menu']['Клюшки']['(HS TACKS YTH) Клюшки']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Клюшки']['(HS TACKS YTH) Клюшки'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в категорию 'Клюшки'")
    elif callback.data in file['general_menu']['Клюшки']['(TRIGGER 6 PRO) Клюшки']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Клюшки']['(TRIGGER 6 PRO) Клюшки'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в категорию 'Клюшки'")
    elif callback.data in file['general_menu']['Клюшки']['(Вратарские) Клюшки']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Клюшки']['(Вратарские) Клюшки'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в категорию 'Клюшки'")
    elif callback.data in file['general_menu']['Клюшки']['(Деревянные ULTIMATE) Клюшки']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Клюшки']['(Деревянные ULTIMATE) Клюшки'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в категорию 'Клюшки'")
    elif callback.data in file['general_menu']['Клюшки']['(Другие) Клюшки']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Клюшки']['(Другие) Клюшки'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в категорию 'Клюшки'")

    elif callback.data in file['general_menu']['Коньки']['(9350) Коньки']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Коньки']['(9350) Коньки'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в категорию 'Коньки'")
    elif callback.data in file['general_menu']['Коньки']['(9360) Коньки']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Коньки']['(9360) Коньки'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в категорию 'Коньки'")
    elif callback.data in file['general_menu']['Коньки']['(9370) Коньки']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Коньки']['(9370) Коньки'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в категорию 'Коньки'")
    elif callback.data in file['general_menu']['Коньки']['(9380) Коньки']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Коньки']['(9380) Коньки'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в категорию 'Коньки'")
    elif callback.data in file['general_menu']['Коньки']['(AS3) Коньки']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Коньки']['(AS3) Коньки'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в категорию 'Коньки'")
    elif callback.data in file['general_menu']['Коньки']['(AS3 PRO) Коньки']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Коньки']['(AS3 PRO) Коньки'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в категорию 'Коньки'")
    elif callback.data in file['general_menu']['Коньки']['(BAUER) Коньки']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Коньки']['(BAUER) Коньки'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в категорию 'Коньки'")
    elif callback.data in file['general_menu']['Коньки']['(FT2) Коньки']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Коньки']['(FT2) Коньки'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в категорию 'Коньки'")
    elif callback.data in file['general_menu']['Коньки']['(FT460) Коньки']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Коньки']['(FT460) Коньки'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в категорию 'Коньки'")
    elif callback.data in file['general_menu']['Коньки']['(FT475) Коньки']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Коньки']['(FT475) Коньки'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в категорию 'Коньки'")
    elif callback.data in file['general_menu']['Коньки']['(SK FT4) Коньки']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Коньки']['(SK FT4) Коньки'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в категорию 'Коньки'")
    elif callback.data in file['general_menu']['Коньки']['(SK FT4PRO) Коньки']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Коньки']['(SK FT4PRO) Коньки'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в категорию 'Коньки'")
    elif callback.data in file['general_menu']['Коньки']['(SK RIB 100K PRO) Коньки']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Коньки']['(SK RIB 100K PRO) Коньки'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в категорию 'Коньки'")
    elif callback.data in file['general_menu']['Коньки']['(SK RIB 86K) Коньки']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Коньки']['(SK RIB 86K) Коньки'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в категорию 'Коньки'")
    elif callback.data in file['general_menu']['Коньки']['(SK RIB 90K) Коньки']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Коньки']['(SK RIB 90K) Коньки'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в категорию 'Коньки'")
    elif callback.data in file['general_menu']['Коньки']['(Вратарские) Коньки']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Коньки']['(Вратарские) Коньки'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в категорию 'Коньки'")
    elif callback.data in file['general_menu']['Коньки']['(Фигурные) Коньки']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Коньки']['(Фигурные) Коньки'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в категорию 'Коньки'")
    elif callback.data in file['general_menu']['Коньки']['(Другие) Коньки']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Коньки']['(Другие) Коньки'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в категорию 'Коньки'")

    elif callback.data in file['general_menu']['Перчатки']['(4R) Перчатки']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Перчатки']['(4R) Перчатки'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в категорию 'Перчатки'")
    elif callback.data in file['general_menu']['Перчатки']['(9040) Перчатки']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Перчатки']['(9040) Перчатки'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в категорию 'Перчатки'")
    elif callback.data in file['general_menu']['Перчатки']['(9060) Перчатки']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Перчатки']['(9060) Перчатки'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в категорию 'Перчатки'")
    elif callback.data in file['general_menu']['Перчатки']['(9080) Перчатки']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Перчатки']['(9080) Перчатки'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в категорию 'Перчатки'")
    elif callback.data in file['general_menu']['Перчатки']['(BAUER) Перчатки']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Перчатки']['(BAUER) Перчатки'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в категорию 'Перчатки'")
    elif callback.data in file['general_menu']['Перчатки']['(EASTON) Перчатки']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Перчатки']['(EASTON) Перчатки'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в категорию 'Перчатки'")
    elif callback.data in file['general_menu']['Перчатки']['(HG 475) Перчатки']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Перчатки']['(HG 475) Перчатки'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в категорию 'Перчатки'")
    elif callback.data in file['general_menu']['Перчатки']['(HG 485) Перчатки']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Перчатки']['(HG 485) Перчатки'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в категорию 'Перчатки'")
    elif callback.data in file['general_menu']['Перчатки']['(HG FT4 PRO) Перчатки']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Перчатки']['(HG FT4 PRO) Перчатки'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в категорию 'Перчатки'")
    elif callback.data in file['general_menu']['Перчатки']['(SHER-WOOD) Перчатки']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Перчатки']['(SHER-WOOD) Перчатки'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в категорию 'Перчатки'")
    elif callback.data in file['general_menu']['Перчатки']['(Другие) Перчатки']:
        tovar_name = tovar(callback.data)
        source = (file['general_menu']['Перчатки']['(Другие) Перчатки'][callback.data])
        article = source[0]
        image = source[1]
        opisanie = source[2]
        price = source[3]
        bot.send_message(callback.message.chat.id, 'Секунду..')
        poisk_tovar_in_base(bot, callback.message, article, tovar_name.tovar, image=image, opisanie=opisanie,
                            price=price).poisk_ostatok(back_value="Назад в категорию 'Перчатки'")

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
    zayavka_done(bot=bot, message=message, quantity=quantity.quantity, article=article)


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


