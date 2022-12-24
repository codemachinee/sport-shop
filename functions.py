from telebot import types
# библиотека работы с гугл таблицами
import gspread
# библиотека проверки даты
from datetime import *
# библиотека рандома
from random import *
import json
from passwords import *
from yoomoney import Client, Quickpay


ostatok = None
admin_id = igor
file = json.load(open('categories_dict.json', 'rb'))  # файл хранящий структуру категорий товаров


class buttons:  # класс для создания клавиатур различных категорий товаров
    global file, tovar_row

    def __init__(self, bot, message, file=file, key='general_menu', kategoriya=None,
                 image='https://drive.google.com/file/d/1nG0RvJ9L6Ez_O9SOjllhFn2OvszB92TE/view?usp=share_link'):
        self.bot = bot
        self.message = message
        self.key = key
        self.file = file[self.key]  # выбор в файле конкретной категории по ключу (возвращает список)
        self.kategoriya = kategoriya  # уровень меню (категории/подкатегории/товары)
        self.image = image

    def menu_buttons(self):
        kb1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        but1 = types.KeyboardButton(text='Категории товаров 🗂️')
        but2 = types.KeyboardButton(text='История заказов 📋')
        but3 = types.KeyboardButton(text='Корзина 🗑️')
        but4 = types.KeyboardButton(text='Вопросы-ответы ⁉️')
        but5 = types.KeyboardButton(text='Контакты ☎️')
        kb1.add(but1, but2, but3, but4, but5)
        self.bot.send_message(self.message.chat.id, text='...', reply_markup=kb1)

    def marks_buttons(self):  # функция создающая клавиатуру
        keys = {}
        kb1 = types.InlineKeyboardMarkup()
        self.file = list(self.file.keys())
        for i in self.file:
            keys[f'but{self.file.index(i)}'] = types.InlineKeyboardButton(text=i, callback_data=i)
            if self.file.index(i) > 0 and self.file.index(i) % 2 != 0:
                if len(i) <= 16 and len(self.file[self.file.index(i) - 1]) <= 16:
                    kb1.add(keys[f'but{self.file.index(i) - 1}'], keys[f'but{self.file.index(i)}'])  # , row_width=1)
                else:
                    kb1.add(keys[f'but{self.file.index(i) - 1}'])
                    kb1.add(keys[f'but{self.file.index(i)}'])
            elif self.file.index(i) == (len(self.file) - 1):
                kb1.add(keys[f'but{self.file.index(i)}'])
        self.bot.send_photo(self.message.chat.id, photo=self.image)
        self.bot.send_message(self.message.chat.id, text=f'Пожалуйста выберите {self.kategoriya}', reply_markup=kb1)

    def zayavka_buttons(self, back_value='Вернуться в начало'):
        kb4 = types.InlineKeyboardMarkup(row_width=1)
        but1 = types.InlineKeyboardButton(text='Оформить заявку!', callback_data='Да, хочу!')
        but3 = types.InlineKeyboardButton(text='Вернуться назад', callback_data=back_value)
        kb4.add(but1, but3)
        self.bot.send_message(self.message.chat.id, f'Хотите оформить заявку/купить онлайн выбранный товар?\n '
                                                    f'/help - справка по боту', reply_markup=kb4)

    def basket_buttons(self, name=None, r=None):
        keys = {}
        kb4 = types.InlineKeyboardMarkup()
        for i in r:
            keys[f'but{r.index(i)}'] = types.InlineKeyboardButton(text=name[r.index(i)], callback_data=f'delete_row{i}')
            kb4.add(keys[f'but{r.index(i)}'])
        self.bot.send_message(self.message.chat.id, f'Для удаления заявки выберите товар:', reply_markup=kb4)

    def oplata_buttons(self, article, back_value='Вернуться в начало'):
        kb5 = types.InlineKeyboardMarkup(row_width=1)
        but1 = types.InlineKeyboardButton(text='Оплатить онлайн (-5%)!',
                                          url=platezhy(self.bot, self.message, article=article).url_generation())
        but2 = types.InlineKeyboardButton(text='Я оплатил, что дальше?', callback_data='Оплачено')
        but3 = types.InlineKeyboardButton(text='Оплатить позже', callback_data='Не оплачено')
        but4 = types.InlineKeyboardButton(text='Вернуться назад', callback_data=back_value)
        kb5.add(but1, but2, but3, but4)
        try:
            self.bot.send_message(self.message.chat.id, f'Выберите способ оплаты. После оформления заявки с Вами свяжется '
                                                        f'менеджер для уточнения деталей. (Выбор '
                                                        f'количества далее)\n '
                                                        f'/help - справка по боту', reply_markup=kb5)
        except AttributeError:
            self.bot.send_message(self.message.message.chat.id,
                                  f'Выберите способ оплаты. После оформления заявки с Вами свяжется '
                                  f'менеджер для уточнения деталей. (Выбор '
                                  f'количества далее)\n '
                                  f'/help - справка по боту', reply_markup=kb5)


def zayavka_done(bot, message, quantity, article):
    global ostatok
    try:
        int(quantity)

        if int(quantity) <= int(ostatok) and int(quantity) != 0:
            buttons(bot, message).oplata_buttons(article=article)
        else:
            bot.send_message(message.chat.id,
                             f'Увы, но указанное количество либо превышает остатки товара, либо равно 0. Отправьте '
                             f'корректное значение.\n'
                             f'Чтобы изменить товар выберите "Категории товаров 🗂️"')
            buttons(bot, message).zayavka_buttons()
    except ValueError:
        bot.send_message(message.chat.id, f'Пожалуйста, укажите количество ЧИСЛОМ')
        buttons(bot, message).zayavka_buttons()


class poisk_tovar_in_base:
    def __init__(self, bot, message, article='0', tovar_name=None, quantity=None, image=None, opisanie=None,
                 price=None):
        self.bot = bot
        self.message = message
        self.article = article
        self.tovar_name = tovar_name
        self.quantity = quantity
        self.image = image
        self.opisanie = opisanie
        self.price = price
        gc = gspread.service_account(
            filename='pidor-of-the-day-af3dd140b860.json')  # доступ к гугл табл по ключевому файлу аккаунта разраба
        # открытие таблицы по юрл адресу:
        try:
            sh = gc.open('CCM')
            self.worksheet = sh.worksheet('остатки')  # выбор листа 'общая база клиентов' таблицы
            self.worksheet2 = sh.worksheet('заявки')
        except Exception:
            self.bot.send_message(self.message.chat.id, 'Ошибка подключения. Повторите запрос через 1 минуту.')


    def poisk_ostatok(self, back_value='Вернуться в начало'):
        cell = self.worksheet.find(self.article, in_column=0)  # поиск ячейки с данными по ключевому слову
        global file_open, opisanie, ostatok
        try:
            self.bot.send_message(self.message.chat.id, 'Проверяем наличие..')
            # запись клиента в свободную строку базы старых клиентов:
            self.bot.send_photo(self.message.chat.id, self.image, self.opisanie)
            self.bot.send_message(self.message.chat.id, f'В наличии: {self.worksheet.cell(cell.row, 5).value[0:-4]}\n'
                                                        f'{self.price}')
            if self.worksheet.cell(cell.row, 5).value[0:-4] == '0':
                kb4 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
                but1 = types.KeyboardButton(text='Вернуться в начало')
                kb4.add(but1)
                self.bot.send_message(self.message.chat.id, f'Увы товар закончился\n'
                                                            f'/help - справка по боту\n', reply_markup=kb4)
            else:
                buttons(self.bot, self.message).zayavka_buttons(back_value=back_value)
                ostatok = self.worksheet.cell(cell.row, 5).value[0:-4]
        except AttributeError:
            self.bot.send_message(self.message.chat.id, 'Ошибка, товар отсутствует')

    def zayavka_v_baze(self):  # функция перевода из базы потенциальных клиентов в базу старых клиентов
        cell = self.worksheet.find(self.article, in_column=0)  # поиск ячейки с данными по ключевому слову
        cell_id = (self.worksheet2.findall(str(self.message.message.chat.id), in_column=1))[::-1]
        try:
            for i in cell_id:
                if self.worksheet2.cell(i.row, 9).value == 'FALSE' and self.worksheet2.cell(i.row,
                                                                                            8).value == self.article:
                    self.worksheet2.update(f'F{i.row}:G{i.row}',
                                           [[int(self.worksheet2.cell(i.row, 6).value) + int(self.quantity),
                                             str(datetime.now().date())]])
                    update_ostatok = int(self.worksheet.cell(cell.row, 5).value[0:-4]) - int(self.quantity)
                    self.worksheet.update(f"E{cell.row}", [[update_ostatok]])
                    self.bot.send_message(admin_id, 'Заявка внесена в базу ✅\n'
                                                    'смотреть базу: https://docs.google.com/spreadsheets/d/'
                                                    '14P5j3t4Z9kmy4o87WEbLqeTwsKi7YZAx7RiQPlY2c1w/edit?usp=sharing')
                    break
            else:
                worksheet_len2 = len(self.worksheet2.col_values(1)) + 1
                # запись клиента в свободную строку базы старых клиентов:
                self.worksheet2.update(f'A{worksheet_len2}:I{worksheet_len2}',
                                       [[self.message.message.chat.id, self.message.from_user.username,
                                         self.message.from_user.first_name, self.message.from_user.last_name,
                                         self.tovar_name, self.quantity, str(datetime.now().date()), self.article, False]])
                update_ostatok = int(self.worksheet.cell(cell.row, 5).value[0:-4]) - int(self.quantity)
                self.worksheet.update(f"E{cell.row}", [[update_ostatok]])  # удаление клиента из базы потенциальных
                self.bot.send_message(admin_id, 'Заявка внесена в базу ✅\n'
                                                'смотреть базу: https://docs.google.com/spreadsheets/d/'
                                                '14P5j3t4Z9kmy4o87WEbLqeTwsKi7YZAx7RiQPlY2c1w/edit?usp=sharing')
        except AttributeError:
            self.bot.send_message(admin_id, 'Ошибка добавления заявки в базу')

    def basket_search(self):
        name = []
        r = []
        self.bot.send_message(self.message.chat.id, "Собираем данные..")
        cell_id = (self.worksheet2.findall(str(self.message.chat.id), in_column=1))[::-1]
        for i in cell_id:
            if self.worksheet2.cell(i.row, 9).value == 'FALSE':
                name.append(f'\n{self.worksheet2.cell(i.row, 5).value} - {self.worksheet2.cell(i.row, 6).value} шт.\n')
                r.append(i.row)

        name_ = ' '.join(name)
        if len(name) != 0:
            self.bot.send_message(self.message.chat.id, f'На данный момент в обработке следующие заявки:\n'
                                                        f'{name_}')
            buttons(self.bot, self.message).basket_buttons(name, r)
        else:
            self.bot.send_message(self.message.chat.id, f'Товары отсутствуют..Проверьте историю заказов.')

    def basket_delete(self, row):
        try:
            cell = self.worksheet.find(self.worksheet2.cell(row, 8).value, in_column=0)
            update_ostatok = int(self.worksheet.cell(cell.row, 5).value[0:-4]) + int(self.worksheet2.cell(row, 6).value)
            self.worksheet.update(f"E{cell.row}", [[update_ostatok]])
            self.worksheet2.batch_clear([f"A{row}:H{row}"])
            self.bot.send_message(self.message.message.chat.id, 'Товар успешно удаленн из корзины')
            self.bot.send_message(admin_id, f'🚨!!!ВНИМАНИЕ!!!🚨\n'
                                            f'Клиент отменил заявку\n'
                                            f'id чата: {self.message.message.chat.id}\n'
                                            f'Имя: {self.message.from_user.first_name}\n'
                                            f'Фамилия: {self.message.from_user.last_name}\n'
                                            f'Ссылка: @{self.message.from_user.username}\n'
                                            f'/sent_message - отправить сообщение клиенту от имени бота\n'
                                            f'/help - cправка по боту')
        except AttributeError:
            self.bot.send_message(self.message.message.chat.id, 'Товар уже был удален ранее. Перейдите в корзину снова, чтобы '
                                                        'обновить данные')

    def zakazy_search(self):
        name = []
        r = []
        self.bot.send_message(self.message.chat.id, "Собираем данные..")
        cell_id = (self.worksheet2.findall(str(self.message.chat.id), in_column=1))
        for i in cell_id:
            if self.worksheet2.cell(i.row, 9).value == 'TRUE':
                name.append(f'\n({self.worksheet2.cell(i.row, 7).value}) {self.worksheet2.cell(i.row, 5).value} - '
                            f'{self.worksheet2.cell(i.row, 6).value} шт.\n')
        name = ' '.join(name)
        if len(name) != 0:
            self.bot.send_message(self.message.chat.id, f'Ваша история заказов:\n'
                                                        f'{name}')
        else:
            self.bot.send_message(self.message.chat.id, f'Заказы отсутствуют')


class tovar:  # класс хранения сообщения для рассылки
    def __init__(self, tovar):
        self.tovar = tovar

    def _get_tovar_(self):
        return self.tovar


class Quantity:  # класс хранения сообщения для рассылки
    def __init__(self, quantity):
        self.quantity = quantity

    def get_quantity(self):
        return self.quantity


class rasylka_message:  # класс хранения сообщения для рассылки
    def __init__(self, post):
        self.post = post

    def _get_message_(self):
        return self.post


class platezhy:
    def __init__(self, bot, message, article, tovar_name=None, quantity=0):
        self.bot = bot
        self.message = message
        self.article = article
        self.tovar_name = tovar_name
        self.quantity = quantity
        try:
            self.marker_mess = self.message.chat.id + int(self.article[0:-4])
        except AttributeError:
            self.marker_mess = self.message.message.chat.id + int(self.article[0:-4])

    def url_generation(self):
        try:
            quickpay = Quickpay(
                receiver="4100116460956966",
                quickpay_form="shop",
                targets="payment",
                paymentType="SB",
                sum=10,
                label=self.marker_mess
            )
            return quickpay.base_url
        except AttributeError:
            quickpay = Quickpay(
                receiver="4100116460956966",
                quickpay_form="shop",
                targets="payment",
                paymentType="SB",
                sum=10,
                label=self.marker_mess
            )
            return quickpay.base_url

    def chec_control(self):
        token = "4100116460956966.47E0EA43A8D91E10F709F2EB8566AF852B8A37BB682D92179C76F70872D7BCB47F1649F0F31CC6B2AB4" \
                "D4F33EFCB9FD6200045936DD3CDFE5E9E70B7CBA5AFF18056C02C1EAA8630938EDCFA04D8A11CA5AA70775A9CFD95CD82A1C" \
                "A82DF5851C66DC4A2522C1FBD01F16CDF5AADD56E55081CC2CD8A0360CC353103964BED59"
        client = Client(token)
        try:
            history = client.operation_history(label=self.marker_mess)
        except AttributeError:
            history = client.operation_history(label=self.marker_mess)
        try:
            if (int(datetime.now().time().hour * 3600 + datetime.now().time().minute * 60 + datetime.now().time().second) -
                    int(history.operations[0].datetime.time().hour * 3600 + history.operations[0].datetime.minute * 60 +
                        history.operations[0].datetime.time().second)) <= 12600:        # 3 часа 30 мин
                self.bot.send_message(self.message.message.chat.id,
                                          f'Заявка оформлена и передана менеджеру, с Вами свяжутся в ближайшее время. '
                                          'Спасибо, что выбрали нас.🤝\n'
                                          f'Чтобы продолжить покупки выберите "Категории товаров 🗂️"')
                self.bot.send_message(admin_id, f'🚨!!!ВНИМАНИЕ!!!🚨\n'
                                               f'Поступила ЗАЯВКА от:\n'
                                               f'id чата: {self.message.message.chat.id}\n'
                                               f'Имя: {self.message.from_user.first_name}\n'
                                               f'Фамилия: {self.message.from_user.last_name}\n'
                                               f'Ссылка: @{self.message.from_user.username}\n'
                                               f'Товар: {self.tovar_name}\n'
                                               f'Количество: {self.quantity}\n')
                poisk_tovar_in_base(self.bot, self.message, self.article, self.tovar_name, self.quantity).zayavka_v_baze()
            else:
                self.bot.send_message(self.message.message.chat.id, 'Платеж не был подтвержден. Если Вы оплатили товар, '
                                                                    'напишите в поддержку @hloapps')
                buttons(self.bot, self.message).oplata_buttons(article=self.article)
        except IndexError:
            self.bot.send_message(self.message.message.chat.id, 'Платеж не найден. Если Вы оплатили товар, '
                                                                'напишите в поддержку @hloapps')
            buttons(self.bot, self.message).oplata_buttons(article=self.article)

