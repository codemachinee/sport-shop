#import gspread
import json
import pandas as pd

#print('Введите строку начала:')
start_row = 319
#print('Введите строку конца:')
end_row = 326
#print('Введите url картинки:')
photo = 'https:'
#print('Введите начало среза названия:')
start_slice_of_name = int(11)
#print('Введите конец среза названия:')
end_slice_of_name = int(14)
#print('Введите конец среза описания:')
end_slice_of_description = int(6)

with open('categories_dict.json', 'r', encoding='UTF-8') as file:  #открытие json файла и преобразование в словарь питона
    src = file.read()
    new_file = json.loads(src)

worksheet_article = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[0])
worksheet_name = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[1])

new_file['general_menu']['Вратарская экипировка'].update({'Блин вратаря':
                                                   {"Назад в категорию 'Вратарская экипировка'": []}})
for i in range(start_row, end_row + 1):
    name = str(worksheet_name[i-2:i-1].values.item())
    article = str(f'{worksheet_article[i-2:i-1].values.item()},000')
    new_file['general_menu']['Вратарская экипировка']['Блин вратаря'][name[start_slice_of_name:(- end_slice_of_name)]] = \
        [article, photo, 'Описание: ' + name[:(- end_slice_of_description)],
         'Цена:']

with open('categories_dict.json', 'w', encoding='UTF-8') as file:
    json.dump(new_file, file, indent=4, ensure_ascii=False)
########################################################################################################################

#print('Введите строку начала:')
start_row = 334
#print('Введите строку конца:')
end_row = 338
#print('Введите url картинки:')
photo = 'https:'
#print('Введите начало среза названия:')
start_slice_of_name = int(16)
#print('Введите конец среза названия:')
end_slice_of_name = int(6)
#print('Введите конец среза описания:')
end_slice_of_description = int(6)

with open('categories_dict.json', 'r', encoding='UTF-8') as file:  #открытие json файла и преобразование в словарь питона
    src = file.read()
    new_file = json.loads(src)

worksheet_article = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[0])
worksheet_name = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[1])

new_file['general_menu']['Вратарская экипировка'].update({'Панцырь-нагрудник':
                                                   {"Назад в категорию 'Вратарская экипировка'": []}})
for i in range(start_row, end_row + 1):
    name = str(worksheet_name[i-2:i-1].values.item())
    article = str(f'{worksheet_article[i-2:i-1].values.item()},000')
    new_file['general_menu']['Вратарская экипировка']['Панцырь-нагрудник'][name[start_slice_of_name:(- end_slice_of_name)]] = \
        [article, photo, 'Описание: ' + name[:(- end_slice_of_description)],
         'Цена:']

with open('categories_dict.json', 'w', encoding='UTF-8') as file:
    json.dump(new_file, file, indent=4, ensure_ascii=False)
########################################################################################################################

#print('Введите строку начала:')
start_row = 348
#print('Введите строку конца:')
end_row = 351
#print('Введите url картинки:')
photo = 'https:'
#print('Введите начало среза названия:')
start_slice_of_name = int(13)
#print('Введите конец среза названия:')
end_slice_of_name = int(12)
#print('Введите конец среза описания:')
end_slice_of_description = int(6)

with open('categories_dict.json', 'r', encoding='UTF-8') as file:  #открытие json файла и преобразование в словарь питона
    src = file.read()
    new_file = json.loads(src)

worksheet_article = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[0])
worksheet_name = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[1])

new_file['general_menu']['Вратарская экипировка'].update({'Шлем':
                                                   {"Назад в категорию 'Вратарская экипировка'": []}})
for i in range(start_row, end_row + 1):
    name = str(worksheet_name[i-2:i-1].values.item())
    article = str(f'{worksheet_article[i-2:i-1].values.item()},000')
    new_file['general_menu']['Вратарская экипировка']['Шлем'][name[start_slice_of_name:(- end_slice_of_name)]] = \
        [article, photo, 'Описание: ' + name[:(- end_slice_of_description)],
         'Цена:']

with open('categories_dict.json', 'w', encoding='UTF-8') as file:
    json.dump(new_file, file, indent=4, ensure_ascii=False)
########################################################################################################################

#print('Введите строку начала:')
start_row = 327
#print('Введите строку конца:')
end_row = 332
#print('Введите url картинки:')
photo = 'https:'
#print('Введите начало среза названия:')
start_slice_of_name = int(15)
#print('Введите конец среза названия:')
end_slice_of_name = int(12)
#print('Введите конец среза описания:')
end_slice_of_description = int(6)

with open('categories_dict.json', 'r', encoding='UTF-8') as file:  #открытие json файла и преобразование в словарь питона
    src = file.read()
    new_file = json.loads(src)

worksheet_article = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[0])
worksheet_name = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[1])

for i in range(start_row, end_row + 1):
    name = str(worksheet_name[i-2:i-1].values.item())
    article = str(f'{worksheet_article[i-2:i-1].values.item()},000')
    new_file['general_menu']['Вратарская экипировка'][name[start_slice_of_name:(- end_slice_of_name)]] = \
        [article, photo, 'Описание: ' + name[:(- end_slice_of_description)],
         'Цена:']

with open('categories_dict.json', 'w', encoding='UTF-8') as file:
    json.dump(new_file, file, indent=4, ensure_ascii=False)
########################################################################################################################

#print('Введите строку начала:')
start_row = 339
#print('Введите строку конца:')
end_row = 346
#print('Введите url картинки:')
photo = 'https:'
#print('Введите начало среза названия:')
start_slice_of_name = int(16)
#print('Введите конец среза названия:')
end_slice_of_name = int(12)
#print('Введите конец среза описания:')
end_slice_of_description = int(6)

with open('categories_dict.json', 'r', encoding='UTF-8') as file:  #открытие json файла и преобразование в словарь питона
    src = file.read()
    new_file = json.loads(src)

worksheet_article = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[0])
worksheet_name = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[1])

for i in range(start_row, end_row + 1):
    name = str(worksheet_name[i-2:i-1].values.item())
    article = str(f'{worksheet_article[i-2:i-1].values.item()},000')
    new_file['general_menu']['Вратарская экипировка'][name[start_slice_of_name:(- end_slice_of_name)]] = \
        [article, photo, 'Описание: ' + name[:(- end_slice_of_description)],
         'Цена:']

with open('categories_dict.json', 'w', encoding='UTF-8') as file:
    json.dump(new_file, file, indent=4, ensure_ascii=False)
########################################################################################################################

#print('Введите строку начала:')
start_row = 353
#print('Введите строку конца:')
end_row = 355
#print('Введите url картинки:')
photo = 'https:'
#print('Введите начало среза названия:')
start_slice_of_name = int(14)
#print('Введите конец среза названия:')
end_slice_of_name = int(14)
#print('Введите конец среза описания:')
end_slice_of_description = int(6)

with open('categories_dict.json', 'r', encoding='UTF-8') as file:  #открытие json файла и преобразование в словарь питона
    src = file.read()
    new_file = json.loads(src)

worksheet_article = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[0])
worksheet_name = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[1])

for i in range(start_row, end_row + 1):
    name = str(worksheet_name[i-2:i-1].values.item())
    article = str(f'{worksheet_article[i-2:i-1].values.item()},000')
    new_file['general_menu']['Вратарская экипировка'][name[start_slice_of_name:(- end_slice_of_name)]] = \
        [article, photo, 'Описание: ' + name[:(- end_slice_of_description)],
         'Цена:']

with open('categories_dict.json', 'w', encoding='UTF-8') as file:
    json.dump(new_file, file, indent=4, ensure_ascii=False)
########################################################################################################################

