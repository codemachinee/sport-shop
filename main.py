# библиотека телеграм-бота
import telebot
# с помощью типов можно создавать клавиатуры
from telebot import types
# библиотека для выполнения фоновых процессов в определенное время
#from apscheduler.schedulers.background import BackgroundScheduler
# импорт из файла functions
from functions import buttons, zayavka_done, poisk_tovar_in_base, tovar, Quantity, rasylka_message

#token = '5380562272:AAFqodiUpENCtx7oD8f5xnbIDNOoxJW6YMY'
token = '5108031210:AAFO7ACd3yHNEhYIc7OVl-6G4dviPSZNA_8'
bot = telebot.TeleBot(token)

tovar_name = None
quantity = None
rassylka = None


@bot.message_handler(commands=['start'])    # перехватчик команды /start
def start(message):
    kb2 = types.ReplyKeyboardRemove()    # удаление клавиатуры
    bot.send_message(message.chat.id, '...', reply_markup=kb2)
    file_open = open("start_logo.png", 'rb')    # открытие и чтение файла стартовой картинки
    bot.send_photo(message.chat.id, file_open, '''Здравствуйте!
Вас приветствует CCM_bot - Я помогу подобрать профессиональный хоккейный инвентарь для хоккея по лучшим ценам. 🏆🏒🥇

/category - асоортимент по категориям
/help - все возможности бота''')


@bot.message_handler(commands=['help'])
def help(message):
    kb2 = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, '...', reply_markup=kb2)
    if message.chat.id == 1338281106:      # условия демонстрации различных команд для админа и клиентов
        bot.send_message(message.chat.id, f'Основные команды поддерживаемые ботом:\n'
                                          f'/category - ассортимент товара по категориям\n'
                                          f'/start - инициализация бота\n'
                                          f'/help - справка по боту\n'
                                          f'/sent_message - отправить с помощью бота сообщение клиенту по id чата')
    else:
        bot.send_message(message.chat.id, f'Основные команды поддерживаемые ботом:\n'
                                          f'/category - ассортимент товара по категориям\n'
                                          f'/start - инициализация бота\n'
                                          f'/help - справка по боту\n')


@bot.message_handler(commands=['category'])
def price(message):
    buttons(bot, message, key='general_menu', kategoriya='категорию').marks_buttons() # класс по формированию различных клавиатур, располагается в functions


@bot.message_handler(commands=['sent_message'])  # команда для переброски клиента из базы потенциальных клиентов в
def sent_message(message):    # базу старых клиентов
    if message.chat.id == 1338281106:
        sent = bot.send_message('1338281106', 'Введи id чата клиента, которому нужно написать от лица бота')
        bot.register_next_step_handler(sent, sent_message_perehvat_1)   # перехватывает ответ пользователя на сообщение "sent" и
                                                              # и направляет его аргументом в функцию base_perehvat
    else:
        bot.send_message(message.chat.id, 'У Вас нет прав для использования данной команды')


@bot.message_handler(func=lambda m: m.text)  # перехватчик текстовых сообщений
def chek_message_category(m):
    global tovar_name
    global quantity
    if m.text == 'Вернуться в начало':
        buttons(bot, m, key='general_menu', kategoriya='категорию').marks_buttons()
    if m.text == "Вернуться в категорию 'Клюшки'":
        buttons(bot, m, key='Kлюшки', kategoriya='подкатегорию').marks_buttons()
    if m.text == 'Другое':
        buttons(bot, m, key='Другое', kategoriya='подкатегорию').marks_buttons()
    if m.text == 'Да, хочу!':
        val = bot.send_message(m.chat.id, 'Пожалуйста отправьте количество желаемого товара ЧИСЛОМ с помощью клавиатуры')
        bot.register_next_step_handler(val, amount) # функция оформления заявки. Отправляет админу специальное сообщение о заявке
    if m.text == 'Kоньки':
        buttons(bot, m, key='Kоньки', kategoriya='подкатегорию').marks_buttons()
    if m.text == 'Kлюшки':
        buttons(bot, m, key='Kлюшки', kategoriya='подкатегорию').marks_buttons()
    if m.text == 'Защита':
        buttons(bot, m, key='Защита', kategoriya='подкатегорию').marks_buttons()
    if m.text == 'Вратарям':
        buttons(bot, m, key='Вратарям', kategoriya='подкатегорию').marks_buttons()
    if m.text == 'Одежда':
        buttons(bot, m, key='Одежда', kategoriya='подкатегорию').marks_buttons()
    if m.text == 'Хоккейная форма':
        buttons(bot, m, key='Хоккейная форма', kategoriya='подкатегорию').marks_buttons()
    if m.text == 'Аксессуары':
        buttons(bot, m, key='Аксессуары', kategoriya='подкатегорию').marks_buttons()
    if m.text == 'Ленты для клюшек':
        buttons(bot, m, key='Ленты для клюшек', kategoriya='товар').marks_buttons()
    if m.text == 'Надставки':
        buttons(bot, m, key='Надставки', kategoriya='товар').marks_buttons()
    if m.text == 'Клюшки':
        buttons(bot, m, key='Клюшки', kategoriya='товар').marks_buttons()
    if m.text == 'Красная лента (L)':
        tovar_name = tovar(m.text)
        poisk_tovar_in_base(bot, m, tovar_name.tovar).poisk_ostatok()
    if m.text == 'Красная лента (N SZ)':
        tovar_name = tovar(m.text)
        poisk_tovar_in_base(bot, m, tovar_name.tovar).poisk_ostatok()
    if m.text == 'Черная лента (L)':
        tovar_name = tovar(m.text)
        poisk_tovar_in_base(bot, m, tovar_name.tovar).poisk_ostatok()
    if m.text == 'Черная лента (N SZ)':
        tovar_name = tovar(m.text)
        poisk_tovar_in_base(bot, m, tovar_name.tovar).poisk_ostatok()


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
    global quantity
    quantity = Quantity(message.text)
    zayavka_done(bot=bot, message=message, tovar_name=tovar_name.tovar, quantity=quantity.quantity)


def sent_message_perehvat_1(message):
    try:
        global rasylka
        rasylka = rasylka_message(message.text)  # хз почему message.id а не message.text но bot.copy_message() работает только так
        sent = bot.send_message('1338281106', 'Введите текст сообщения')
        bot.register_next_step_handler(sent, sent_message_perehvat_2)
    except ValueError:
        bot.send_message('1338281106', 'Неккоректное значение. Воспользуйтесь командой /sent_message еще раз')


def sent_message_perehvat_2(message):
    kb2 = types.ReplyKeyboardRemove()
    global rasylka
    bot.copy_message(rasylka.post, '1338281106', message.id, reply_markup=kb2)
    bot.send_message('1338281106', 'Сообщение отправлено!')


bot.infinity_polling()


