import gspread
import json

file = open('categories_dict.json', 'rb')  # файл хранящий структуру категорий товаров
file = json.load(file)  # открытие файла
#file = (file['general_menu']['Ворота']['Ворота SH MINI STEEL 3x2 Bauer Street Brana'])[0]

file = str(file).find('general_menu')
print(file)

gc = gspread.service_account(
            filename='pidor-of-the-day-af3dd140b860.json')  # доступ к гугл табл по ключевому файлу аккаунта разраба
        # открытие таблицы по юрл адресу:
sh = gc.open('CCM')
worksheet = sh.worksheet('Лист3')
worksheet1 = sh.worksheet('заявки')
a = worksheet.get_all_values()
with open('_dict.json', 'w') as file:
    json.dump(a, file, indent=4, ensure_ascii=False)

d = {}
d{'клюшки': 12, 'коньки': 5}
