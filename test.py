import gspread
import json

file = open('categories_dict.json', 'rb')  # файл хранящий структуру категорий товаров
file = json.load(file)  # открытие файла
#file = (file['general_menu']['Ворота']['Ворота SH MINI STEEL 3x2 Bauer Street Brana'])[0]

file = str(file).find('general_menu')
print(file)
