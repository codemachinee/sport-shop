import gspread
import json

#print('Введите строку начала:')
start_row = 559
#print('Введите строку конца:')
end_row = 561
#print('Введите url картинки:')
photo = 'https://hockey-overtime.ru/upload/iblock/bfd/bfd21f38b040a540a556d404903b3a31.jpeg'
#print('Введите начало среза названия:')
start_slice_of_name = int(13)
#print('Введите конец среза названия:')
end_slice_of_name = int(13)
#print('Введите конец среза описания:')
end_slice_of_description = int(6)

with open('categories_dict.json', 'r', encoding='UTF-8') as file:  #открытие json файла и преобразование в словарь питона
    src = file.read()
    new_file = json.loads(src)

gc = gspread.service_account(filename='pidor-of-the-day-af3dd140b860.json')  # доступ к листу гугл таблицы
sh = gc.open('CCM')
worksheet = sh.worksheet('остатки')


new_file['general_menu']['Защита']['Трусы'].update({'(HP FT4 PRO)':
                                                   {"Назад в подкатегорию 'Трусы'": []}})
for i in range(start_row, end_row + 1):
    new_file['general_menu']['Защита']['Трусы']['(HP FT4 PRO)'][str(worksheet.cell(i, 2).
                                                                               value[start_slice_of_name:
                                                                                     (- end_slice_of_name)])] = \
        [worksheet.cell(i, 1).value, photo, 'Описание: ' + worksheet.cell(i, 2).value[:(- end_slice_of_description)],
         'Цена:']

    #new_file['general_menu']['Защита']['Трусы'][str(worksheet.cell(i, 2).
     #                                                                          value[start_slice_of_name:
      #                                                                               (- end_slice_of_name)])] = \
       # [worksheet.cell(i, 1).value, photo, 'Описание: ' + worksheet.cell(i, 2).value[:(- end_slice_of_description)],
        # 'Цена:']

with open('categories_dict.json', 'w', encoding='UTF-8') as file:
    json.dump(new_file, file, indent=4, ensure_ascii=False)
########################################################################################################################

#print('Введите строку начала:')
start_row = 563
#print('Введите строку конца:')
end_row = 567
#print('Введите url картинки:')
photo = 'https://avatars.mds.yandex.net/get-marketpic/1714105/market_u5yt8Otl0Q9Tsw0Mop9gLQ/600x800'
#print('Введите начало среза названия:')
start_slice_of_name = int(13)
#print('Введите конец среза названия:')
end_slice_of_name = int(13)
#print('Введите конец среза описания:')
end_slice_of_description = int(6)

with open('categories_dict.json', 'r', encoding='UTF-8') as file:  #открытие json файла и преобразование в словарь питона
    src = file.read()
    new_file = json.loads(src)

gc = gspread.service_account(filename='pidor-of-the-day-af3dd140b860.json')  # доступ к листу гугл таблицы
sh = gc.open('CCM')
worksheet = sh.worksheet('остатки')


new_file['general_menu']['Защита']['Трусы'].update({'(FT370) Трусы':
                                                   {"Назад в подкатегорию 'Трусы'": []}})
for i in range(start_row, end_row + 1):
    new_file['general_menu']['Защита']['Трусы']['(FT370) Трусы'][str(worksheet.cell(i, 2).
                                                                               value[start_slice_of_name:
                                                                                     (- end_slice_of_name)])] = \
        [worksheet.cell(i, 1).value, photo, 'Описание: ' + worksheet.cell(i, 2).value[:(- end_slice_of_description)],
         'Цена:']

    #new_file['general_menu']['Защита']['Трусы'][str(worksheet.cell(i, 2).
     #                                                                          value[start_slice_of_name:
      #                                                                               (- end_slice_of_name)])] = \
       # [worksheet.cell(i, 1).value, photo, 'Описание: ' + worksheet.cell(i, 2).value[:(- end_slice_of_description)],
        # 'Цена:']

with open('categories_dict.json', 'w', encoding='UTF-8') as file:
    json.dump(new_file, file, indent=4, ensure_ascii=False)

########################################################################################################################

#print('Введите строку начала:')
start_row = 569
#print('Введите строку конца:')
end_row = 570
#print('Введите url картинки:')
photo = 'https://avatars.mds.yandex.net/get-mpic/5312993/img_id3298435409184826108.jpeg/orig'
#print('Введите начало среза названия:')
start_slice_of_name = int(13)
#print('Введите конец среза названия:')
end_slice_of_name = int(13)
#print('Введите конец среза описания:')
end_slice_of_description = int(6)

with open('categories_dict.json', 'r', encoding='UTF-8') as file:  #открытие json файла и преобразование в словарь питона
    src = file.read()
    new_file = json.loads(src)

gc = gspread.service_account(filename='pidor-of-the-day-af3dd140b860.json')  # доступ к листу гугл таблицы
sh = gc.open('CCM')
worksheet = sh.worksheet('остатки')

for i in range(start_row, end_row + 1):
    new_file['general_menu']['Защита']['Трусы'][str(worksheet.cell(i, 2).
                                                                               value[start_slice_of_name:
                                                                                     (- end_slice_of_name)])] = \
        [worksheet.cell(i, 1).value, photo, 'Описание: ' + worksheet.cell(i, 2).value[:(- end_slice_of_description)],
         'Цена:']

with open('categories_dict.json', 'w', encoding='UTF-8') as file:
    json.dump(new_file, file, indent=4, ensure_ascii=False)

########################################################################################################################

#print('Введите строку начала:')
start_row = 572
#print('Введите строку конца:')
end_row = 576
#print('Введите url картинки:')
photo = 'https://avatars.mds.yandex.net/get-mpic/5324096/img_id5041677470786723392.jpeg/orig'
#print('Введите начало среза названия:')
start_slice_of_name = int(13)
#print('Введите конец среза названия:')
end_slice_of_name = int(14)
#print('Введите конец среза описания:')
end_slice_of_description = int(6)

with open('categories_dict.json', 'r', encoding='UTF-8') as file:  #открытие json файла и преобразование в словарь питона
    src = file.read()
    new_file = json.loads(src)

gc = gspread.service_account(filename='pidor-of-the-day-af3dd140b860.json')  # доступ к листу гугл таблицы
sh = gc.open('CCM')
worksheet = sh.worksheet('остатки')


new_file['general_menu']['Защита']['Трусы'].update({'(HP 485) Трусы':
                                                   {"Назад в подкатегорию 'Трусы'": []}})
for i in range(start_row, end_row + 1):
    new_file['general_menu']['Защита']['Трусы']['(HP 485) Трусы'][str(worksheet.cell(i, 2).
                                                                               value[start_slice_of_name:
                                                                                     (- end_slice_of_name)])] = \
        [worksheet.cell(i, 1).value, photo, 'Описание: ' + worksheet.cell(i, 2).value[:(- end_slice_of_description)],
         'Цена:']

    #new_file['general_menu']['Защита']['Трусы'][str(worksheet.cell(i, 2).
     #                                                                          value[start_slice_of_name:
      #                                                                               (- end_slice_of_name)])] = \
       # [worksheet.cell(i, 1).value, photo, 'Описание: ' + worksheet.cell(i, 2).value[:(- end_slice_of_description)],
        # 'Цена:']

with open('categories_dict.json', 'w', encoding='UTF-8') as file:
    json.dump(new_file, file, indent=4, ensure_ascii=False)

########################################################################################################################

#print('Введите строку начала:')
start_row = 578
#print('Введите строку конца:')
end_row = 580
#print('Введите url картинки:')
photo = 'https://www.mhockey.ru/upload/iblock/038/038707c07169e454a14af2436b5637b5.jpg'
#print('Введите начало среза названия:')
start_slice_of_name = int(13)
#print('Введите конец среза названия:')
end_slice_of_name = int(14)
#print('Введите конец среза описания:')
end_slice_of_description = int(6)

with open('categories_dict.json', 'r', encoding='UTF-8') as file:  #открытие json файла и преобразование в словарь питона
    src = file.read()
    new_file = json.loads(src)

gc = gspread.service_account(filename='pidor-of-the-day-af3dd140b860.json')  # доступ к листу гугл таблицы
sh = gc.open('CCM')
worksheet = sh.worksheet('остатки')


new_file['general_menu']['Защита']['Трусы'].update({'(HP FT4) Трусы':
                                                   {"Назад в подкатегорию 'Трусы'": []}})
for i in range(start_row, end_row + 1):
    new_file['general_menu']['Защита']['Трусы']['(HP FT4) Трусы'][str(worksheet.cell(i, 2).
                                                                               value[start_slice_of_name:
                                                                                     (- end_slice_of_name)])] = \
        [worksheet.cell(i, 1).value, photo, 'Описание: ' + worksheet.cell(i, 2).value[:(- end_slice_of_description)],
         'Цена:']

    #new_file['general_menu']['Защита']['Трусы'][str(worksheet.cell(i, 2).
     #                                                                          value[start_slice_of_name:
      #                                                                               (- end_slice_of_name)])] = \
       # [worksheet.cell(i, 1).value, photo, 'Описание: ' + worksheet.cell(i, 2).value[:(- end_slice_of_description)],
        # 'Цена:']

with open('categories_dict.json', 'w', encoding='UTF-8') as file:
    json.dump(new_file, file, indent=4, ensure_ascii=False)

########################################################################################################################

#print('Введите строку начала:')
start_row = 582
#print('Введите строку конца:')
end_row = 588
#print('Введите url картинки:')
photo = 'https://hockeyclub.ru/upload/resize_cache/iblock/7af/1000_1000_1/IMG_6414.jpg'
#print('Введите начало среза названия:')
start_slice_of_name = int(13)
#print('Введите конец среза названия:')
end_slice_of_name = int(14)
#print('Введите конец среза описания:')
end_slice_of_description = int(6)

with open('categories_dict.json', 'r', encoding='UTF-8') as file:  #открытие json файла и преобразование в словарь питона
    src = file.read()
    new_file = json.loads(src)

gc = gspread.service_account(filename='pidor-of-the-day-af3dd140b860.json')  # доступ к листу гугл таблицы
sh = gc.open('CCM')
worksheet = sh.worksheet('остатки')


new_file['general_menu']['Защита']['Трусы'].update({'(HP FT4 PRO) Трусы':
                                                   {"Назад в подкатегорию 'Трусы'": []}})
for i in range(start_row, end_row + 1):
    new_file['general_menu']['Защита']['Трусы']['(HP FT4 PRO) Трусы'][str(worksheet.cell(i, 2).
                                                                               value[start_slice_of_name:
                                                                                     (- end_slice_of_name)])] = \
        [worksheet.cell(i, 1).value, photo, 'Описание: ' + worksheet.cell(i, 2).value[:(- end_slice_of_description)],
         'Цена:']

    #new_file['general_menu']['Защита']['Трусы'][str(worksheet.cell(i, 2).
     #                                                                          value[start_slice_of_name:
      #                                                                               (- end_slice_of_name)])] = \
       # [worksheet.cell(i, 1).value, photo, 'Описание: ' + worksheet.cell(i, 2).value[:(- end_slice_of_description)],
        # 'Цена:']

with open('categories_dict.json', 'w', encoding='UTF-8') as file:
    json.dump(new_file, file, indent=4, ensure_ascii=False)

########################################################################################################################

#print('Введите строку начала:')
start_row = 582
#print('Введите строку конца:')
end_row = 588
#print('Введите url картинки:')
photo = 'https://hockeyclub.ru/upload/resize_cache/iblock/7af/1000_1000_1/IMG_6414.jpg'
#print('Введите начало среза названия:')
start_slice_of_name = int(13)
#print('Введите конец среза названия:')
end_slice_of_name = int(14)
#print('Введите конец среза описания:')
end_slice_of_description = int(6)

with open('categories_dict.json', 'r', encoding='UTF-8') as file:  #открытие json файла и преобразование в словарь питона
    src = file.read()
    new_file = json.loads(src)

gc = gspread.service_account(filename='pidor-of-the-day-af3dd140b860.json')  # доступ к листу гугл таблицы
sh = gc.open('CCM')
worksheet = sh.worksheet('остатки')


new_file['general_menu']['Защита']['Трусы'].update({'(HP FT4 PRO) Трусы':
                                                   {"Назад в подкатегорию 'Трусы'": []}})
for i in range(start_row, end_row + 1):
    new_file['general_menu']['Защита']['Трусы']['(HP FT4 PRO) Трусы'][str(worksheet.cell(i, 2).
                                                                               value[start_slice_of_name:
                                                                                     (- end_slice_of_name)])] = \
        [worksheet.cell(i, 1).value, photo, 'Описание: ' + worksheet.cell(i, 2).value[:(- end_slice_of_description)],
         'Цена:']

    #new_file['general_menu']['Защита']['Трусы'][str(worksheet.cell(i, 2).
     #                                                                          value[start_slice_of_name:
      #                                                                               (- end_slice_of_name)])] = \
       # [worksheet.cell(i, 1).value, photo, 'Описание: ' + worksheet.cell(i, 2).value[:(- end_slice_of_description)],
        # 'Цена:']

with open('categories_dict.json', 'w', encoding='UTF-8') as file:
    json.dump(new_file, file, indent=4, ensure_ascii=False)