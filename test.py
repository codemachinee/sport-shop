import gspread
import json

file = open('categories_dict.json', 'rb')  # файл хранящий структуру категорий товаров
file = json.load(file)  # открытие файла
file = (file['general_menu']['Ворота']['Ворота SH MINI STEEL 3x2 Bauer Street Brana'])[0]

#print(int('9065,000'[0:-4]))

gc = gspread.service_account(
            filename='pidor-of-the-day-af3dd140b860.json')  # доступ к гугл табл по ключевому файлу аккаунта разраба
        # открытие таблицы по юрл адресу:
sh = gc.open('CCM')
quantity = '1'
worksheet = sh.worksheet('остатки')  # выбор листа 'общая база клиентов' таблицы
worksheet2 = sh.worksheet('заявки')
cell = worksheet.find('10338,000', in_column=0)
update_ostatok = int(worksheet.cell(cell.row, 5).value[0:-4]) - int(quantity)
worksheet.update(f"E{cell.row}", [[update_ostatok]])
print(update_ostatok)
print(cell)
