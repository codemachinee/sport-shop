import gspread
import json

with open('categories_dict.json', 'r') as file:  #открытие json файла и преобразование в словарь питона
    src = file.read()
    new_file = json.loads(src)

gc = gspread.service_account(filename='pidor-of-the-day-af3dd140b860.json')  # доступ к листу гугл таблицы
sh = gc.open('CCM')
worksheet = sh.worksheet('остатки')

photo = 'https://cdn.shoplightspeed.com/shops/617630/files/23727444/ccm-epft1-js-yt-elbow-pads-v1-l.jpg'


new_file['general_menu']['Защита']['Налокотники'].update({'(FT1) Налокотники':
                                                         {"Назад в подкатегорию 'Налокотники'": []}})
for i in range(486, 489):
    new_file['general_menu']['Защита']['Налокотники']['(FT1) Налокотники'][str(worksheet.cell(i, 2).value[:-13])]\
        = [worksheet.cell(i, 1).value, photo,
           'Описание: ' + worksheet.cell(i, 2).value[:-6], 'Цена:']
with open('categories_dict.json', 'w') as file:
    json.dump(new_file, file, indent=4, ensure_ascii=False)

#for i in range(480, 485):
 #   new_file['general_menu']['Защита']['Налокотники']['(EP FT485) Налокотники'] = {worksheet.cell(i, 2).value[12:-14]: [worksheet.cell(i, 1).value, photo, 'Описание: ' + worksheet.cell(i, 2).value[:-6], 'Цена:']}
#with open('new.json', 'w') as file:
 #   json.dump(new_file, file, indent=4, ensure_ascii=False)
