#import gspread
import pandas as pd
import json

#print('Введите строку начала:')
start_row = 925
#print('Введите строку конца:')
end_row = 931
#print('Введите url картинки:')
photo = 'https://drive.google.com/file/d/1PQk9qBGAubAhc_eC3aCvvAE4rr4zHkoe/view?usp=share_link'
#print('Введите начало среза названия:')
start_slice_of_name = int(19)
#print('Введите конец среза названия:')
end_slice_of_name = int(14)
#print('Введите конец среза описания:')
end_slice_of_description = int(6)

with open('categories_dict.json', 'r', encoding='UTF-8') as file:  #открытие json файла и преобразование в словарь питона
    src = file.read()
    new_file = json.loads(src)

worksheet_article = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[0])
worksheet_name = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[1])

new_file['general_menu']['Клюшки'].update({'(AS4 PRO) Клюшки': {"Назад в категорию 'Клюшки'": []}})

for i in range(start_row, end_row + 1):
    name = str(worksheet_name[i-2:i-1].values.item())
    article = str(f'{worksheet_article[i-2:i-1].values.item()},000')
    new_file['general_menu']['Клюшки']['(AS4 PRO) Клюшки'][name[start_slice_of_name:(- end_slice_of_name)]] = \
        [article, photo, 'Описание: ' + name[:(- end_slice_of_description)],
         'Цена:']

with open('categories_dict.json', 'w', encoding='UTF-8') as file:
    json.dump(new_file, file, indent=4, ensure_ascii=False)
########################################################################################################################

#print('Введите строку начала:')
start_row = 933
#print('Введите строку конца:')
end_row = 936
#print('Введите url картинки:')
photo = 'https://drive.google.com/file/d/1PQk9qBGAubAhc_eC3aCvvAE4rr4zHkoe/view?usp=share_link'
#print('Введите начало среза названия:')
start_slice_of_name = int(7)
#print('Введите конец среза названия:')
end_slice_of_name = int(14)
#print('Введите конец среза описания:')
end_slice_of_description = int(6)

with open('categories_dict.json', 'r', encoding='UTF-8') as file:  #открытие json файла и преобразование в словарь питона
    src = file.read()
    new_file = json.loads(src)

worksheet_article = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[0])
worksheet_name = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[1])

new_file['general_menu']['Клюшки'].update({'(BAUER) Клюшки': {"Назад в категорию 'Клюшки'": []}})

for i in range(start_row, end_row + 1):
    name = str(worksheet_name[i-2:i-1].values.item())
    article = str(f'{worksheet_article[i-2:i-1].values.item()},000')
    new_file['general_menu']['Клюшки']['(BAUER) Клюшки'][name[start_slice_of_name:(- end_slice_of_name)]] = \
        [article, photo, 'Описание: ' + name[:(- end_slice_of_description)],
         'Цена:']

with open('categories_dict.json', 'w', encoding='UTF-8') as file:
    json.dump(new_file, file, indent=4, ensure_ascii=False)
########################################################################################################################

#print('Введите строку начала:')
start_row = 942
#print('Введите строку конца:')
end_row = 944
#print('Введите url картинки:')
photo = 'https://drive.google.com/file/d/1PQk9qBGAubAhc_eC3aCvvAE4rr4zHkoe/view?usp=share_link'
#print('Введите начало среза названия:')
start_slice_of_name = int(19)
#print('Введите конец среза названия:')
end_slice_of_name = int(14)
#print('Введите конец среза описания:')
end_slice_of_description = int(6)

with open('categories_dict.json', 'r', encoding='UTF-8') as file:  #открытие json файла и преобразование в словарь питона
    src = file.read()
    new_file = json.loads(src)

worksheet_article = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[0])
worksheet_name = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[1])

new_file['general_menu']['Клюшки'].update({'(HS FT5) Клюшки': {"Назад в категорию 'Клюшки'": []}})

for i in range(start_row, end_row + 1):
    name = str(worksheet_name[i-2:i-1].values.item())
    article = str(f'{worksheet_article[i-2:i-1].values.item()},000')
    new_file['general_menu']['Клюшки']['(HS FT5) Клюшки'][name[start_slice_of_name:(- end_slice_of_name)]] = \
        [article, photo, 'Описание: ' + name[:(- end_slice_of_description)],
         'Цена:']

with open('categories_dict.json', 'w', encoding='UTF-8') as file:
    json.dump(new_file, file, indent=4, ensure_ascii=False)
########################################################################################################################

#print('Введите строку начала:')
start_row = 952
#print('Введите строку конца:')
end_row = 954
#print('Введите url картинки:')
photo = 'https://drive.google.com/file/d/1PQk9qBGAubAhc_eC3aCvvAE4rr4zHkoe/view?usp=share_link'
#print('Введите начало среза названия:')
start_slice_of_name = int(19)
#print('Введите конец среза названия:')
end_slice_of_name = int(14)
#print('Введите конец среза описания:')
end_slice_of_description = int(6)

with open('categories_dict.json', 'r', encoding='UTF-8') as file:  #открытие json файла и преобразование в словарь питона
    src = file.read()
    new_file = json.loads(src)

worksheet_article = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[0])
worksheet_name = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[1])

new_file['general_menu']['Клюшки'].update({'(HS TACKS YTH) Клюшки': {"Назад в категорию 'Клюшки'": []}})

for i in range(start_row, end_row + 1):
    name = str(worksheet_name[i-2:i-1].values.item())
    article = str(f'{worksheet_article[i-2:i-1].values.item()},000')
    new_file['general_menu']['Клюшки']['(HS TACKS YTH) Клюшки'][name[start_slice_of_name:(- end_slice_of_name)]] = \
        [article, photo, 'Описание: ' + name[:(- end_slice_of_description)],
         'Цена:']

with open('categories_dict.json', 'w', encoding='UTF-8') as file:
    json.dump(new_file, file, indent=4, ensure_ascii=False)
########################################################################################################################

#print('Введите строку начала:')
start_row = 970
#print('Введите строку конца:')
end_row = 974
#print('Введите url картинки:')
photo = 'https://drive.google.com/file/d/1PQk9qBGAubAhc_eC3aCvvAE4rr4zHkoe/view?usp=share_link'
#print('Введите начало среза названия:')
start_slice_of_name = int(19)
#print('Введите конец среза названия:')
end_slice_of_name = int(14)
#print('Введите конец среза описания:')
end_slice_of_description = int(6)

with open('categories_dict.json', 'r', encoding='UTF-8') as file:  #открытие json файла и преобразование в словарь питона
    src = file.read()
    new_file = json.loads(src)

worksheet_article = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[0])
worksheet_name = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[1])

new_file['general_menu']['Клюшки'].update({'(TRIGGER 6 PRO) Клюшки': {"Назад в категорию 'Клюшки'": []}})

for i in range(start_row, end_row + 1):
    name = str(worksheet_name[i-2:i-1].values.item())
    article = str(f'{worksheet_article[i-2:i-1].values.item()},000')
    new_file['general_menu']['Клюшки']['(TRIGGER 6 PRO) Клюшки'][name[start_slice_of_name:(- end_slice_of_name)]] = \
        [article, photo, 'Описание: ' + name[:(- end_slice_of_description)],
         'Цена:']

with open('categories_dict.json', 'w', encoding='UTF-8') as file:
    json.dump(new_file, file, indent=4, ensure_ascii=False)
########################################################################################################################

#print('Введите строку начала:')
start_row = 976
#print('Введите строку конца:')
end_row = 987
#print('Введите url картинки:')
photo = 'https://drive.google.com/file/d/1PQk9qBGAubAhc_eC3aCvvAE4rr4zHkoe/view?usp=share_link'
#print('Введите начало среза названия:')
start_slice_of_name = int(15)
#print('Введите конец среза названия:')
end_slice_of_name = int(14)
#print('Введите конец среза описания:')
end_slice_of_description = int(6)

with open('categories_dict.json', 'r', encoding='UTF-8') as file:  #открытие json файла и преобразование в словарь питона
    src = file.read()
    new_file = json.loads(src)

worksheet_article = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[0])
worksheet_name = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[1])

new_file['general_menu']['Клюшки'].update({'(Вратарские) Клюшки': {"Назад в категорию 'Клюшки'": []}})

for i in range(start_row, end_row + 1):
    name = str(worksheet_name[i-2:i-1].values.item())
    article = str(f'{worksheet_article[i-2:i-1].values.item()},000')
    new_file['general_menu']['Клюшки']['(Вратарские) Клюшки'][name[start_slice_of_name:(- end_slice_of_name)]] = \
        [article, photo, 'Описание: ' + name[:(- end_slice_of_description)],
         'Цена:']

with open('categories_dict.json', 'w', encoding='UTF-8') as file:
    json.dump(new_file, file, indent=4, ensure_ascii=False)
########################################################################################################################

#print('Введите строку начала:')
start_row = 989
#print('Введите строку конца:')
end_row = 992
#print('Введите url картинки:')
photo = 'https://drive.google.com/file/d/1PQk9qBGAubAhc_eC3aCvvAE4rr4zHkoe/view?usp=share_link'
#print('Введите начало среза названия:')
start_slice_of_name = int(19)
#print('Введите конец среза названия:')
end_slice_of_name = int(12)
#print('Введите конец среза описания:')
end_slice_of_description = int(6)

with open('categories_dict.json', 'r', encoding='UTF-8') as file:  #открытие json файла и преобразование в словарь питона
    src = file.read()
    new_file = json.loads(src)

worksheet_article = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[0])
worksheet_name = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[1])

new_file['general_menu']['Клюшки'].update({'(деревянные ULTIMATE) Клюшки': {"Назад в категорию 'Клюшки'": []}})

for i in range(start_row, end_row + 1):
    name = str(worksheet_name[i-2:i-1].values.item())
    article = str(f'{worksheet_article[i-2:i-1].values.item()},000')
    new_file['general_menu']['Клюшки']['(деревянные ULTIMATE) Клюшки'][name[start_slice_of_name:(- end_slice_of_name)]] = \
        [article, photo, 'Описание: ' + name[:(- end_slice_of_description)],
         'Цена:']

with open('categories_dict.json', 'w', encoding='UTF-8') as file:
    json.dump(new_file, file, indent=4, ensure_ascii=False)
########################################################################################################################
#print('Введите строку начала:')
#start_row = 989
#print('Введите строку конца:')
#end_row = 992
#print('Введите url картинки:')
photo = 'https://drive.google.com/file/d/1PQk9qBGAubAhc_eC3aCvvAE4rr4zHkoe/view?usp=share_link'
#print('Введите начало среза названия:')
start_slice_of_name = int(19)
#print('Введите конец среза названия:')
end_slice_of_name = int(14)
#print('Введите конец среза описания:')
end_slice_of_description = int(6)

with open('categories_dict.json', 'r', encoding='UTF-8') as file:  #открытие json файла и преобразование в словарь питона
    src = file.read()
    new_file = json.loads(src)

worksheet_article = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[0])
worksheet_name = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[1])

new_file['general_menu']['Клюшки'].update({'(Другие) Клюшки': {"Назад в категорию 'Клюшки'": []}})

for i in (905, 907, 909, 911, 912, 914, 916, 917, 919, 920, 922, 923, 938, 940, 946, 948, 950, 956, 957, 959, 960, 962, 963, 966, 968):
    name = str(worksheet_name[i-2:i-1].values.item())
    article = str(f'{worksheet_article[i-2:i-1].values.item()},000')
    new_file['general_menu']['Клюшки']['(Другие) Клюшки'][name[start_slice_of_name:(- end_slice_of_name)]] = \
        [article, photo, 'Описание: ' + name[:(- end_slice_of_description)], 'Цена:']

with open('categories_dict.json', 'w', encoding='UTF-8') as file:
    json.dump(new_file, file, indent=4, ensure_ascii=False)
########################################################################################################################
