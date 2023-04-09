import gspread  # библиотека работы с гугл таблицами
from telebot import types
from datetime import *  # библиотека проверки даты
# from random import *
from passwords import *
# from yoomoney import Client, Quickpay
from openpyxl import load_workbook  # библиотека работы с exel таблицами


tovar_descriptions = None
ostatok = None
admin_id = igor
# file = json.load(open('categories_dict.json', 'rb'))  # файл хранящий структуру категорий товаров


class buttons:  # класс для создания клавиатур различных категорий товаров
    global file, tovar_row

    def __init__(self, bot, message, kategoriya=None, list_one=None,
                 image='https://drive.google.com/file/d/1nG0RvJ9L6Ez_O9SOjllhFn2OvszB92TE/view?usp=share_link'):
        self.bot = bot
        self.message = message
        self.image = image
        self.kategoriya = kategoriya
        self.list_one = list_one

    def menu_buttons(self):
        kb1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
        but1 = types.KeyboardButton(text='Каталог 🗂️')
        but2 = types.KeyboardButton(text='Поступления 🆕')
        but3 = types.KeyboardButton(text='Распродажа 🏷️')
        but4 = types.KeyboardButton(text='О нас ⁉️')
        but5 = types.KeyboardButton(text='Мои заказы 📋')
        but6 = types.KeyboardButton(text='Корзина 🗑️')
        kb1.add(but1, but2, but3, but4, but5, but6)
        self.bot.send_message(self.message.chat.id, text='...', reply_markup=kb1)

    def razdely_buttons(self):
        keys = {}
        kb1 = types.InlineKeyboardMarkup()
        for i in self.list_one:
            keys[f'but{self.list_one.index(i)}'] = types.InlineKeyboardButton(text=i, callback_data=i)
            if self.list_one.index(i) > 0 and self.list_one.index(i) % 2 != 0:
                if len(i) <= 16 and len(self.list_one[self.list_one.index(i) - 1]) <= 16:
                    kb1.add(keys[f'but{self.list_one.index(i) - 1}'], keys[f'but{self.list_one.index(i)}'])  # , row_width=1)
                else:
                    kb1.add(keys[f'but{self.list_one.index(i) - 1}'])
                    kb1.add(keys[f'but{self.list_one.index(i)}'])
            elif self.list_one.index(i) == (len(self.list_one) - 1):
                kb1.add(keys[f'but{self.list_one.index(i)}'])
        self.bot.send_photo(self.message.chat.id, photo=self.image)
        self.bot.send_message(self.message.chat.id, text=f'Пожалуйста выберите {self.kategoriya}', reply_markup=kb1)

    def marks_buttons(self):  # функция создающая клавиатуру
        keys = {}
        kb1 = types.InlineKeyboardMarkup()
        for i in self.list_one:
            keys[f'but{self.list_one.index(i)}'] = types.InlineKeyboardButton(text=i[0], callback_data=i[1])
            if self.list_one.index(i) > 0 and self.list_one.index(i) % 2 != 0:
                if len(i[0]) <= 16 and len(self.list_one[self.list_one.index(i) - 1][0]) <= 16:
                    kb1.add(keys[f'but{self.list_one.index(i) - 1}'],
                            keys[f'but{self.list_one.index(i)}'])  # , row_width=1)
                else:
                    try:
                        kb1.add(keys[f'but{self.list_one.index(i) - 1}'])
                        kb1.add(keys[f'but{self.list_one.index(i)}'])
                    except Exception:
                        self.bot.send_message(admin_id, 'Ошибка!!!Проверьте таблицу на дублирование')
            elif self.list_one.index(i) == (len(self.list_one) - 1):
                kb1.add(keys[f'but{self.list_one.index(i)}'])
        self.bot.send_photo(self.message.chat.id, photo=self.image)
        self.bot.send_message(self.message.chat.id, text=f'Пожалуйста выберите {self.kategoriya}', reply_markup=kb1)

    def zayavka_buttons(self, back_value='Вернуться в начало'):
        kb4 = types.InlineKeyboardMarkup(row_width=1)
        but1 = types.InlineKeyboardButton(text='Оформить заявку!', callback_data='Да, хочу!')
        but3 = types.InlineKeyboardButton(text='Вернуться назад', callback_data=back_value)
        kb4.add(but1, but3)
        self.bot.send_message(self.message.chat.id, f'Хотите оформить заявку/купить онлайн выбранный товар?\n '
                                                    f'/help - справка по боту', reply_markup=kb4)

    def basket_buttons(self, name=None, r=None, article=None):
        keys = {}
        kb4 = types.InlineKeyboardMarkup()
        for i in r:
            keys[f'but{r.index(i)}'] = types.InlineKeyboardButton(text=name[r.index(i)], callback_data=f'delete_row{article[r.index(i)]}')
            kb4.add(keys[f'but{r.index(i)}'])
        self.bot.send_message(self.message.chat.id, f'Для удаления заявки выберите товар:', reply_markup=kb4)

    # def oplata_buttons(self, article, back_value='Вернуться в начало'):
    #     kb5 = types.InlineKeyboardMarkup(row_width=1)
    #     but1 = types.InlineKeyboardButton(text='Оплатить онлайн (-5%)!',
    #                                       url=platezhy(self.bot, self.message, article=article).url_generation())
    #     but2 = types.InlineKeyboardButton(text='Я оплатил, что дальше?', callback_data='Оплачено')
    #     but3 = types.InlineKeyboardButton(text='Оплатить позже', callback_data='Не оплачено')
    #     but4 = types.InlineKeyboardButton(text='Вернуться назад', callback_data=back_value)
    #     kb5.add(but1, but2, but3, but4)
    #     try:
    #         self.bot.send_message(self.message.chat.id, f'Выберите способ оплаты. После оформления заявки с Вами свяжется '
    #                                                     f'менеджер для уточнения деталей. (Выбор '
    #                                                     f'количества далее)\n '
    #                                                     f'/help - справка по боту', reply_markup=kb5)
    #     except AttributeError:
    #         self.bot.send_message(self.message.message.chat.id,
    #                               f'Выберите способ оплаты. После оформления заявки с Вами свяжется '
    #                               f'менеджер для уточнения деталей. (Выбор '
    #                               f'количества далее)\n '
    #                               f'/help - справка по боту', reply_markup=kb5)
    #
    # def without_oplata_buttons(self, article, back_value='Вернуться в начало'):
    #     kb5 = types.InlineKeyboardMarkup(row_width=1)
    #     but1 = types.InlineKeyboardButton(text='Оплатить онлайн (-5%)!',
    #                                       url=platezhy(self.bot, self.message, article=article).url_generation())
    #     but2 = types.InlineKeyboardButton(text='Я оплатил, что дальше?', callback_data='Оплачено')
    #     but3 = types.InlineKeyboardButton(text='Оплатить позже', callback_data='Не оплачено')
    #     but4 = types.InlineKeyboardButton(text='Вернуться назад', callback_data=back_value)
    #     kb5.add(but1, but2, but3, but4)
    #     try:
    #         self.bot.send_message(self.message.chat.id, f'Выберите способ оплаты. После оформления заявки с Вами свяжется '
    #                                                     f'менеджер для уточнения деталей. (Выбор '
    #                                                     f'количества далее)\n '
    #                                                     f'/help - справка по боту', reply_markup=kb5)
    #     except AttributeError:
    #         self.bot.send_message(self.message.message.chat.id,
    #                               f'Выберите способ оплаты. После оформления заявки с Вами свяжется '
    #                               f'менеджер для уточнения деталей. (Выбор '
    #                               f'количества далее)\n '
    #                               f'/help - справка по боту', reply_markup=kb5)


def zayavka_done(bot, message, number):
    global ostatok
    wb = load_workbook('CCM.xlsx')
    ws = wb['кэш']
    for row in ws.iter_rows(min_row=1, max_row=ws.max_row, min_col=1, max_col=7, values_only=True):
        if row[0] == message.chat.id:
            quantity = row[5]
            bot.send_message(message.chat.id,
                             f'Заявка оформлена и передана менеджеру, с Вами свяжутся в ближайшее время. '
                             'Спасибо, что выбрали нас.🤝\n'
                             f'Чтобы продолжить покупки выберите "Категории товаров 🗂️"')
            buttons(bot, message).menu_buttons()
            bot.send_message(admin_id, f'🚨!!!ВНИМАНИЕ!!!🚨\n'
                                       f'Поступила ЗАЯВКА от:\n'
                                       f'id чата: {message.chat.id}\n'
                                       f'Имя: {message.from_user.first_name}\n'
                                       f'Фамилия: {message.from_user.last_name}\n'
                                       f'№ телефона: {number}\n'
                                       f'Ссылка: @{message.from_user.username}\n'
                                       f'Товар: {row[1]}\n'
                                       f'Артикул: {row[2]}\n'
                                       f'Размер: {row[3]}\n'
                                       f'Цена за штуку: {row[4]}\n'
                                       f'Количество: {quantity}\n'
                                       f'ИТОГО: {int(quantity)*(float(row[4][:-2].replace(",", ".").replace(" ", "")))}'
                                       f' ₽')
            poisk_tovar_in_base(bot, message, row[2], row[1], quantity, size=row[3],
                                price=row[4]).zayavka_v_baze(number,
                                                             int(quantity)*(float(row[4][:-2].replace(",", ".").replace(
                                                                 " ", ""))))
            break


class poisk_tovar_in_base:

    def __init__(self, bot, message, article=None, tovar_name=None, vnalichii=None, image=None, size=None,
                 price=None, your_price=None, size_web=None):
        self.bot = bot
        self.message = message
        self.article = article
        self.tovar_name = tovar_name
        self.vnalichii = vnalichii
        self.image = image
        self.size = size
        self.price = price
        self.your_price = your_price
        self.size_web = size_web
        self.wb = load_workbook('CCM.xlsx')
        self.ws = self.wb['кэш']
        self.ws2 = self.wb['МЛ Остатки штаб']
        gc = gspread.service_account(
            filename='pidor-of-the-day-af3dd140b860.json')  # доступ к гугл табл по ключевому файлу аккаунта разраба
        # открытие таблицы по юрл адресу:
        try:
            sh = gc.open('CCM')
            self.worksheet2 = sh.worksheet('заявки')
        except Exception:
            self.bot.send_message(self.message.chat.id, 'Ошибка подключения. Повторите запрос через 1 минуту.')

    def poisk_ostatok(self, back_value='Вернуться в начало'):
        global ostatok, tovar_descriptions
        try:
            self.bot.send_message(self.message.chat.id, 'Проверяем наличие..')
            if self.image is not None:
                self.bot.send_photo(self.message.chat.id, self.image, f'{self.tovar_name}\nРазмер: {self.size}')
                self.bot.send_message(self.message.chat.id, f'В наличии: {self.vnalichii}\nПрайс: {self.price}\n'
                                                            f'Ваша цена: {self.your_price}\n'
                                                            f'Таблица размеров: {self.size_web}')
                if self.ws.max_row >= 10:
                    self.ws.delete_rows(5, self.ws.max_row)
                    self.ws.insert_rows(1)
                    self.ws['A1'] = self.message.chat.id
                    self.ws['B1'] = self.tovar_name
                    self.ws['C1'] = self.article
                    self.ws['D1'] = self.size
                    self.ws['E1'] = self.your_price
                    self.ws['G1'] = self.vnalichii
                    self.bot.send_message(self.message.chat.id, 'загружаем базу данных..')
                    self.ws['H1'] = poisk_tovar_in_base(self.bot, self.message).poisk_number()
                    self.wb.save('CCM.xlsx')
                else:
                    self.ws.insert_rows(1)
                    self.ws['A1'] = self.message.chat.id
                    self.ws['B1'] = self.tovar_name
                    self.ws['C1'] = self.article
                    self.ws['D1'] = self.size
                    self.ws['E1'] = self.your_price
                    self.ws['G1'] = self.vnalichii
                    self.bot.send_message(self.message.chat.id, 'загружаем базу данных..')
                    self.ws['H1'] = poisk_tovar_in_base(self.bot, self.message).poisk_number()
                    self.wb.save('CCM.xlsx')
                if self.vnalichii == 0:
                    kb4 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
                    but1 = types.KeyboardButton(text='Вернуться в начало')
                    kb4.add(but1)
                    self.bot.send_message(self.message.chat.id, f'Увы товар закончился\n'
                                                                f'/help - справка по боту\n', reply_markup=kb4)
                else:
                    buttons(self.bot, self.message).zayavka_buttons(back_value=back_value)
                    ostatok = self.vnalichii
            else:
                self.bot.send_message(self.message.chat.id, f'Фото товара временно отсутствует\n{self.tovar_name}\n'
                                                            f'Размер: {self.size}')
                self.bot.send_message(self.message.chat.id, f'В наличии: {self.vnalichii}\nПрайс: {self.price}\n'
                                                            f'Ваша цена: {self.your_price}\n'
                                                            f'Таблица размеров: {self.size_web}')
                if self.ws.max_row >= 10:
                    self.ws.delete_rows(5, self.ws.max_row)
                    self.ws.insert_rows(1)
                    self.ws['A1'] = self.message.chat.id
                    self.ws['B1'] = self.tovar_name
                    self.ws['C1'] = self.article
                    self.ws['D1'] = self.size
                    self.ws['E1'] = self.your_price
                    self.ws['G1'] = self.vnalichii
                    self.bot.send_message(self.message.chat.id, 'загружаем базу данных..')
                    self.ws['H1'] = poisk_tovar_in_base(self.bot, self.message).poisk_number()
                    self.wb.save('CCM.xlsx')
                else:
                    self.ws.insert_rows(1)
                    self.ws['A1'] = self.message.chat.id
                    self.ws['B1'] = self.tovar_name
                    self.ws['C1'] = self.article
                    self.ws['D1'] = self.size
                    self.ws['E1'] = self.your_price
                    self.ws['G1'] = self.vnalichii
                    self.bot.send_message(self.message.chat.id, 'загружаем базу данных..')
                    self.ws['H1'] = poisk_tovar_in_base(self.bot, self.message).poisk_number()
                    self.wb.save('CCM.xlsx')
                if self.vnalichii == 0:
                    kb4 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
                    but1 = types.KeyboardButton(text='Вернуться в начало')
                    kb4.add(but1)
                    self.bot.send_message(self.message.chat.id, f'Увы товар закончился\n'
                                                                f'/help - справка по боту\n', reply_markup=kb4)
                else:
                    buttons(self.bot, self.message).zayavka_buttons(back_value=back_value)
                    ostatok = self.vnalichii
        except Exception:
            self.bot.send_message(self.message.chat.id, f'Ошибка, товар отсутствует')

    def zayavka_v_baze(self, number, itogo):  # функция перевода из базы потенциальных клиентов в базу старых клиентов
        cell_id = (self.worksheet2.findall(str(self.message.chat.id), in_column=1))[::-1] # поиск ячейки с данными по ключевому слову
        try:
            for i in cell_id:
                if self.worksheet2.cell(i.row, 12).value == 'FALSE' and str(self.worksheet2.cell(i.row, 9).value) == str(self.article):
                    self.worksheet2.update(f'G{i.row}:K{i.row}',
                                           [[int(self.worksheet2.cell(i.row, 7).value) + int(self.vnalichii),
                                             str(datetime.now().date()), self.worksheet2.cell(i.row, 9).value,
                                             self.worksheet2.cell(i.row, 10).value,
                                             (int(self.worksheet2.cell(i.row, 7).value) + int(self.vnalichii)) *
                                             float(self.worksheet2.cell(i.row, 10).value[:-2].replace(",", ".").replace(" ", ""))]])
                    for a in range(1, self.ws2.max_row + 1):
                        if str(self.ws2.cell(a, 1).value) == str(self.article):
                            self.ws2.cell(a, 8).value = int(self.ws2.cell(a, 8).value) - int(self.vnalichii)
                            self.wb.save('CCM.xlsx')
                            self.bot.send_message(admin_id, 'Заявка внесена в базу ✅\n'
                                                            'смотреть базу: https://docs.google.com/spreadsheets/d/'
                                                            '14P5j3t4Z9kmy4o87WEbLqeTwsKi7YZAx7RiQPlY2c1w/edit?usp=sharing')
                            break
                    break
            else:
                worksheet_len2 = len(self.worksheet2.col_values(1)) + 1
                # запись клиента в свободную строку базы старых клиентов:
                self.worksheet2.update(f'A{worksheet_len2}:l{worksheet_len2}',
                                       [[self.message.chat.id, self.message.from_user.username,
                                         self.message.from_user.first_name, self.message.from_user.last_name, number,
                                         self.tovar_name, self.vnalichii, str(datetime.now().date()), self.article,
                                         self.price, itogo, False]])
                for a in range(1, self.ws2.max_row + 1):
                    if str(self.ws2.cell(a, 1).value) == str(self.article):
                        self.ws2.cell(a, 8).value = int(self.ws2.cell(a, 8).value) - int(self.vnalichii)
                        self.wb.save('CCM.xlsx')
                        self.bot.send_message(admin_id, 'Заявка внесена в базу ✅\n'
                                                        'смотреть базу: https://docs.google.com/spreadsheets/d/'
                                                        '14P5j3t4Z9kmy4o87WEbLqeTwsKi7YZAx7RiQPlY2c1w/edit?usp=sharing')
                        break
        except AttributeError:
            self.bot.send_message(admin_id, 'Ошибка добавления заявки в базу')

    def poisk_number(self):
        cell_id = self.worksheet2.find(str(self.message.chat.id), in_column=1)
        if cell_id is not None:
            number = self.worksheet2.cell(cell_id.row, 5).value
            return number
        else:
            return None

    def basket_search(self):
        name = []
        r = []
        article = []
        self.bot.send_message(self.message.chat.id, "Собираем данные..")
        cell_id = (self.worksheet2.findall(str(self.message.chat.id), in_column=1))[::-1]
        for i in cell_id:
            if self.worksheet2.cell(i.row, 12).value == 'FALSE':
                name.append(f'\n{self.worksheet2.cell(i.row, 6).value} - {self.worksheet2.cell(i.row, 7).value} шт.\n')
                r.append(i.row, )
                article.append(self.worksheet2.cell(i.row, 9).value)
        name_ = ' '.join(name)
        if len(name) != 0:
            self.bot.send_message(self.message.chat.id, f'На данный момент в обработке следующие заявки:\n'
                                                        f'{name_}')
            buttons(self.bot, self.message).basket_buttons(name, r, article)
        else:
            self.bot.send_message(self.message.chat.id, f'Товары отсутствуют..Проверьте историю заказов.')

    def basket_delete(self, article):
        try:
            cell_id = self.worksheet2.find(article, in_column=9)
            for a in range(1, self.ws2.max_row + 1):
                if str(self.ws2.cell(a, 1).value) == str(article):
                    self.ws2.cell(a, 8).value = int(self.ws2.cell(a, 8).value) + int(self.worksheet2.cell(cell_id.row, 7).value)
                    self.bot.send_message(self.message.message.chat.id, 'Товар успешно удален из корзины')
                    self.worksheet2.batch_clear([f"A{cell_id.row}:K{cell_id.row}"])
                    self.wb.save('CCM.xlsx')
                    self.bot.send_message(admin_id, f'🚨!!!ВНИМАНИЕ!!!🚨\n'
                                                    f'Клиент отменил заявку\n'
                                                    f'id чата: {self.message.message.chat.id}\n'
                                                    f'Имя: {self.message.from_user.first_name}\n'
                                                    f'Фамилия: {self.message.from_user.last_name}\n'
                                                    f'Ссылка: @{self.message.from_user.username}\n'
                                                    f'/sent_message - отправить сообщение клиенту от имени бота\n'
                                                    f'/help - cправка по боту')
                    break
        except AttributeError:
            self.bot.send_message(self.message.message.chat.id, 'Товар уже был удален ранее. Перейдите в корзину снова, чтобы '
                                                        'обновить данные')

    def zakazy_search(self):
        name = []
        r = []
        self.bot.send_message(self.message.chat.id, "Собираем данные..")
        cell_id = (self.worksheet2.findall(str(self.message.chat.id), in_column=1))
        for i in cell_id:
            if self.worksheet2.cell(i.row, 12).value == 'TRUE':
                name.append(f'\n({self.worksheet2.cell(i.row, 8).value}) {self.worksheet2.cell(i.row, 6).value} - '
                            f'{self.worksheet2.cell(i.row, 7).value} шт.\n')
        name = ' '.join(name)
        if len(name) != 0:
            self.bot.send_message(self.message.chat.id, f'Ваша история заказов:\n'
                                                        f'{name}')
        else:
            self.bot.send_message(self.message.chat.id, f'Заказы отсутствуют')


class rasylka_message:  # класс хранения сообщения для рассылки
    def __init__(self, post):
        self.post = post

    def _get_message_(self):
        return self.post


# class platezhy:
#     def __init__(self, bot, message, article, tovar_name=None, quantity=0):
#         self.bot = bot
#         self.message = message
#         self.article = article
#         self.tovar_name = tovar_name
#         self.quantity = quantity
#         try:
#             self.marker_mess = self.message.chat.id + int(self.article[0:-4])
#         except AttributeError:
#             self.marker_mess = self.message.message.chat.id + int(self.article[0:-4])
#
#     def url_generation(self):
#         try:
#             quickpay = Quickpay(
#                 receiver="4100116460956966",
#                 quickpay_form="shop",
#                 targets="payment",
#                 paymentType="SB",
#                 sum=10,
#                 label=self.marker_mess
#             )
#             return quickpay.base_url
#         except AttributeError:
#             quickpay = Quickpay(
#                 receiver="4100116460956966",
#                 quickpay_form="shop",
#                 targets="payment",
#                 paymentType="SB",
#                 sum=10,
#                 label=self.marker_mess
#             )
#             return quickpay.base_url
#
#     def chec_control(self):
#         token = token_umany
#         client = Client(token)
#         try:
#             history = client.operation_history(label=self.marker_mess)
#         except AttributeError:
#             history = client.operation_history(label=self.marker_mess)
#         try:
#             if (int(datetime.now().time().hour * 3600 + datetime.now().time().minute * 60 + datetime.now().time().second) -
#                     int(history.operations[0].datetime.time().hour * 3600 + history.operations[0].datetime.minute * 60 +
#                         history.operations[0].datetime.time().second)) <= 12600:        # 3 часа 30 мин
#                 self.bot.send_message(self.message.message.chat.id,
#                                           f'Заявка оформлена и передана менеджеру, с Вами свяжутся в ближайшее время. '
#                                           'Спасибо, что выбрали нас.🤝\n'
#                                           f'Чтобы продолжить покупки выберите "Категории товаров 🗂️"')
#                 self.bot.send_message(admin_id, f'🚨!!!ВНИМАНИЕ!!!🚨\n'
#                                                f'Поступила ЗАЯВКА от:\n'
#                                                f'id чата: {self.message.message.chat.id}\n'
#                                                f'Имя: {self.message.from_user.first_name}\n'
#                                                f'Фамилия: {self.message.from_user.last_name}\n'
#                                                f'Ссылка: @{self.message.from_user.username}\n'
#                                                f'Товар: {self.tovar_name}\n'
#                                                f'Количество: {self.quantity}\n')
#                 poisk_tovar_in_base(self.bot, self.message, self.article, self.tovar_name, self.quantity).zayavka_v_baze()
#             else:
#                 self.bot.send_message(self.message.message.chat.id, 'Платеж не был подтвержден. Если Вы оплатили товар, '
#                                                                     'напишите в поддержку @hloapps')
#                 buttons(self.bot, self.message).oplata_buttons(article=self.article)
#         except IndexError:
#             self.bot.send_message(self.message.message.chat.id, 'Платеж не найден. Если Вы оплатили товар, '
#                                                                 'напишите в поддержку @hloapps')
#             buttons(self.bot, self.message).oplata_buttons(article=self.article)


