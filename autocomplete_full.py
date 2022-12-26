#import gspread
import pandas as pd
import json

#print('Введите строку начала:')
start_row = 1437
#print('Введите строку конца:')
end_row = 1446
#print('Введите url картинки:')
photo = 'https://ccm.ru/upload/iblock/144/HG-4-ROLL-PRO2-GLOVES-SR-NV-01.png'
#print('Введите начало среза названия:')
start_slice_of_name = int(16)
#print('Введите конец среза названия:')
end_slice_of_name = int(14)
#print('Введите конец среза описания:')
end_slice_of_description = int(6)

with open('categories_dict.json', 'r', encoding='UTF-8') as file:  #открытие json файла и преобразование в словарь питона
    src = file.read()
    new_file = json.loads(src)

worksheet_article = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[0])
worksheet_name = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[1])

new_file['general_menu']['Перчатки'].update({'(4R) Перчатки': {"Назад в категорию 'Перчатки'": []}})

for i in range(start_row, end_row + 1):
    name = str(worksheet_name[i-2:i-1].values.item())
    article = str(f'{worksheet_article[i-2:i-1].values.item()},000')
    new_file['general_menu']['Перчатки']['(4R) Перчатки'][name[start_slice_of_name:(- end_slice_of_name)]] = \
        [article, photo, 'Описание: ' + name[:(- end_slice_of_description)],
         'Цена:']

with open('categories_dict.json', 'w', encoding='UTF-8') as file:
    json.dump(new_file, file, indent=4, ensure_ascii=False)
########################################################################################################################

#print('Введите строку начала:')
start_row = 1450
#print('Введите строку конца:')
end_row = 1452
#print('Введите url картинки:')
photo = 'https://ccm.ru/upload/iblock/d43/HG9040-JR-CCM-TACKS-Prot-Gloves-BlackWhite-palm.png'
#print('Введите начало среза названия:')
start_slice_of_name = int(16)
#print('Введите конец среза названия:')
end_slice_of_name = int(14)
#print('Введите конец среза описания:')
end_slice_of_description = int(6)

with open('categories_dict.json', 'r', encoding='UTF-8') as file:  #открытие json файла и преобразование в словарь питона
    src = file.read()
    new_file = json.loads(src)

worksheet_article = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[0])
worksheet_name = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[1])

new_file['general_menu']['Перчатки'].update({'(9040) Перчатки': {"Назад в категорию 'Перчатки'": []}})

for i in range(start_row, end_row + 1):
    name = str(worksheet_name[i-2:i-1].values.item())
    article = str(f'{worksheet_article[i-2:i-1].values.item()},000')
    new_file['general_menu']['Перчатки']['(9040) Перчатки'][name[start_slice_of_name:(- end_slice_of_name)]] = \
        [article, photo, 'Описание: ' + name[:(- end_slice_of_description)],
         'Цена:']

with open('categories_dict.json', 'w', encoding='UTF-8') as file:
    json.dump(new_file, file, indent=4, ensure_ascii=False)
########################################################################################################################

#print('Введите строку начала:')
start_row = 1454
#print('Введите строку конца:')
end_row = 1461
#print('Введите url картинки:')
photo = 'https://ccm.ru/upload/iblock/572/HG9060-SR-CCM-TACKS-Prot-Gloves-Navy.png'
#print('Введите начало среза названия:')
start_slice_of_name = int(16)
#print('Введите конец среза названия:')
end_slice_of_name = int(14)
#print('Введите конец среза описания:')
end_slice_of_description = int(6)

with open('categories_dict.json', 'r', encoding='UTF-8') as file:  #открытие json файла и преобразование в словарь питона
    src = file.read()
    new_file = json.loads(src)

worksheet_article = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[0])
worksheet_name = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[1])

new_file['general_menu']['Перчатки'].update({'(9060) Перчатки': {"Назад в категорию 'Перчатки'": []}})

for i in range(start_row, end_row + 1):
    name = str(worksheet_name[i-2:i-1].values.item())
    article = str(f'{worksheet_article[i-2:i-1].values.item()},000')
    new_file['general_menu']['Перчатки']['(9060) Перчатки'][name[start_slice_of_name:(- end_slice_of_name)]] = \
        [article, photo, 'Описание: ' + name[:(- end_slice_of_description)],
         'Цена:']

with open('categories_dict.json', 'w', encoding='UTF-8') as file:
    json.dump(new_file, file, indent=4, ensure_ascii=False)
########################################################################################################################

#print('Введите строку начала:')
start_row = 1463
#print('Введите строку конца:')
end_row = 1467
#print('Введите url картинки:')
photo = 'https://ccm.ru/upload/iblock/148/HG9080-SR-CCM-TACKS-Prot-Gloves-BlackWhite.png'
#print('Введите начало среза названия:')
start_slice_of_name = int(16)
#print('Введите конец среза названия:')
end_slice_of_name = int(14)
#print('Введите конец среза описания:')
end_slice_of_description = int(6)

with open('categories_dict.json', 'r', encoding='UTF-8') as file:  #открытие json файла и преобразование в словарь питона
    src = file.read()
    new_file = json.loads(src)

worksheet_article = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[0])
worksheet_name = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[1])

new_file['general_menu']['Перчатки'].update({'(9080) Перчатки': {"Назад в категорию 'Перчатки'": []}})

for i in range(start_row, end_row + 1):
    name = str(worksheet_name[i-2:i-1].values.item())
    article = str(f'{worksheet_article[i-2:i-1].values.item()},000')
    new_file['general_menu']['Перчатки']['(9080) Перчатки'][name[start_slice_of_name:(- end_slice_of_name)]] = \
        [article, photo, 'Описание: ' + name[:(- end_slice_of_description)],
         'Цена:']

with open('categories_dict.json', 'w', encoding='UTF-8') as file:
    json.dump(new_file, file, indent=4, ensure_ascii=False)
########################################################################################################################

#print('Введите строку начала:')
start_row = 1474
#print('Введите строку конца:')
end_row = 1482
#print('Введите url картинки:')
photo = 'https://drive.google.com/file/d/1PQk9qBGAubAhc_eC3aCvvAE4rr4zHkoe/view?usp=share_link'
#print('Введите начало среза названия:')
start_slice_of_name = int(9)
#print('Введите конец среза названия:')
end_slice_of_name = int(14)
#print('Введите конец среза описания:')
end_slice_of_description = int(6)

with open('categories_dict.json', 'r', encoding='UTF-8') as file:  #открытие json файла и преобразование в словарь питона
    src = file.read()
    new_file = json.loads(src)

worksheet_article = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[0])
worksheet_name = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[1])

new_file['general_menu']['Перчатки'].update({'(BAUER) Перчатки': {"Назад в категорию 'Перчатки'": []}})

for i in range(start_row, end_row + 1):
    name = str(worksheet_name[i-2:i-1].values.item())
    article = str(f'{worksheet_article[i-2:i-1].values.item()},000')
    new_file['general_menu']['Перчатки']['(BAUER) Перчатки'][name[start_slice_of_name:(- end_slice_of_name)]] = \
        [article, photo, 'Описание: ' + name[:(- end_slice_of_description)],
         'Цена:']

with open('categories_dict.json', 'w', encoding='UTF-8') as file:
    json.dump(new_file, file, indent=4, ensure_ascii=False)
########################################################################################################################


#print('Введите строку начала:')
start_row = 1484
#print('Введите строку конца:')
end_row = 1487
#print('Введите url картинки:')
photo = 'https://www.sportdepo.ru/upload/iblock/909/9093ee78b487e232d82b3347b770d5cc.jpeg'
#print('Введите начало среза названия:')
start_slice_of_name = int(9)
#print('Введите конец среза названия:')
end_slice_of_name = int(14)
#print('Введите конец среза описания:')
end_slice_of_description = int(6)

with open('categories_dict.json', 'r', encoding='UTF-8') as file:  #открытие json файла и преобразование в словарь питона
    src = file.read()
    new_file = json.loads(src)

worksheet_article = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[0])
worksheet_name = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[1])

new_file['general_menu']['Перчатки'].update({'(EASTON) Перчатки': {"Назад в категорию 'Перчатки'": []}})

for i in range(start_row, end_row + 1):
    name = str(worksheet_name[i-2:i-1].values.item())
    article = str(f'{worksheet_article[i-2:i-1].values.item()},000')
    new_file['general_menu']['Перчатки']['(EASTON) Перчатки'][name[start_slice_of_name:(- end_slice_of_name)]] = \
        [article, photo, 'Описание: ' + name[:(- end_slice_of_description)],
         'Цена:']

with open('categories_dict.json', 'w', encoding='UTF-8') as file:
    json.dump(new_file, file, indent=4, ensure_ascii=False)
########################################################################################################################

#print('Введите строку начала:')
start_row = 1491
#print('Введите строку конца:')
end_row = 1497
#print('Введите url картинки:')
photo = 'https://ccm.ru/upload/iblock/186/CCM-Gloves-475-NVWH.png'
#print('Введите начало среза названия:')
start_slice_of_name = int(16)
#print('Введите конец среза названия:')
end_slice_of_name = int(14)
#print('Введите конец среза описания:')
end_slice_of_description = int(6)

with open('categories_dict.json', 'r', encoding='UTF-8') as file:  #открытие json файла и преобразование в словарь питона
    src = file.read()
    new_file = json.loads(src)

worksheet_article = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[0])
worksheet_name = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[1])

new_file['general_menu']['Перчатки'].update({'(HG 475) Перчатки': {"Назад в категорию 'Перчатки'": []}})

for i in range(start_row, end_row + 1):
    name = str(worksheet_name[i-2:i-1].values.item())
    article = str(f'{worksheet_article[i-2:i-1].values.item()},000')
    new_file['general_menu']['Перчатки']['(HG 475) Перчатки'][name[start_slice_of_name:(- end_slice_of_name)]] = \
        [article, photo, 'Описание: ' + name[:(- end_slice_of_description)],
         'Цена:']

with open('categories_dict.json', 'w', encoding='UTF-8') as file:
    json.dump(new_file, file, indent=4, ensure_ascii=False)
########################################################################################################################

#print('Введите строку начала:')
start_row = 1499
#print('Введите строку конца:')
end_row = 1506
#print('Введите url картинки:')
photo = 'https://ccm.ru/upload/iblock/019/CCM-Jetspeed-FT485-Senior-Hockey-Gloves-NV-WH.png'
#print('Введите начало среза названия:')
start_slice_of_name = int(16)
#print('Введите конец среза названия:')
end_slice_of_name = int(14)
#print('Введите конец среза описания:')
end_slice_of_description = int(6)

with open('categories_dict.json', 'r', encoding='UTF-8') as file:  #открытие json файла и преобразование в словарь питона
    src = file.read()
    new_file = json.loads(src)

worksheet_article = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[0])
worksheet_name = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[1])

new_file['general_menu']['Перчатки'].update({'(HG 485) Перчатки': {"Назад в категорию 'Перчатки'": []}})

for i in range(start_row, end_row + 1):
    name = str(worksheet_name[i-2:i-1].values.item())
    article = str(f'{worksheet_article[i-2:i-1].values.item()},000')
    new_file['general_menu']['Перчатки']['(HG 485) Перчатки'][name[start_slice_of_name:(- end_slice_of_name)]] = \
        [article, photo, 'Описание: ' + name[:(- end_slice_of_description)],
         'Цена:']

with open('categories_dict.json', 'w', encoding='UTF-8') as file:
    json.dump(new_file, file, indent=4, ensure_ascii=False)
########################################################################################################################

#print('Введите строку начала:')
start_row = 1511
#print('Введите строку конца:')
end_row = 1519
#print('Введите url картинки:')
photo = 'https://ccm.ru/upload/iblock/079/CCM-Jetspeed-FT4-Pro-Senior-Hockey-Gloves-BKWH.jpg'
#print('Введите начало среза названия:')
start_slice_of_name = int(16)
#print('Введите конец среза названия:')
end_slice_of_name = int(14)
#print('Введите конец среза описания:')
end_slice_of_description = int(6)

with open('categories_dict.json', 'r', encoding='UTF-8') as file:  #открытие json файла и преобразование в словарь питона
    src = file.read()
    new_file = json.loads(src)

worksheet_article = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[0])
worksheet_name = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[1])

new_file['general_menu']['Перчатки'].update({'(HG FT4 PRO) Перчатки': {"Назад в категорию 'Перчатки'": []}})

for i in range(start_row, end_row + 1):
    name = str(worksheet_name[i-2:i-1].values.item())
    article = str(f'{worksheet_article[i-2:i-1].values.item()},000')
    new_file['general_menu']['Перчатки']['(HG FT4 PRO) Перчатки'][name[start_slice_of_name:(- end_slice_of_name)]] = \
        [article, photo, 'Описание: ' + name[:(- end_slice_of_description)],
         'Цена:']

with open('categories_dict.json', 'w', encoding='UTF-8') as file:
    json.dump(new_file, file, indent=4, ensure_ascii=False)
########################################################################################################################

#print('Введите строку начала:')
start_row = 1521
#print('Введите строку конца:')
end_row = 1524
#print('Введите url картинки:')
photo = 'https://drive.google.com/file/d/1PQk9qBGAubAhc_eC3aCvvAE4rr4zHkoe/view?usp=share_link'
#print('Введите начало среза названия:')
start_slice_of_name = int(9)
#print('Введите конец среза названия:')
end_slice_of_name = int(6)
#print('Введите конец среза описания:')
end_slice_of_description = int(6)

with open('categories_dict.json', 'r', encoding='UTF-8') as file:  #открытие json файла и преобразование в словарь питона
    src = file.read()
    new_file = json.loads(src)

worksheet_article = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[0])
worksheet_name = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[1])

new_file['general_menu']['Перчатки'].update({'(SHER-WOOD) Перчатки': {"Назад в категорию 'Перчатки'": []}})

for i in range(start_row, end_row + 1):
    name = str(worksheet_name[i-2:i-1].values.item())
    article = str(f'{worksheet_article[i-2:i-1].values.item()},000')
    new_file['general_menu']['Перчатки']['(SHER-WOOD) Перчатки'][name[start_slice_of_name:(- end_slice_of_name)]] = \
        [article, photo, 'Описание: ' + name[:(- end_slice_of_description)],
         'Цена:']

with open('categories_dict.json', 'w', encoding='UTF-8') as file:
    json.dump(new_file, file, indent=4, ensure_ascii=False)
########################################################################################################################

#print('Введите строку начала:')
#start_row = 1521
#print('Введите строку конца:')
#end_row = 1524
#print('Введите url картинки:')
photo = 'https://drive.google.com/file/d/1PQk9qBGAubAhc_eC3aCvvAE4rr4zHkoe/view?usp=share_link'
#print('Введите начало среза названия:')
start_slice_of_name = int(16)
#print('Введите конец среза названия:')
end_slice_of_name = int(14)
#print('Введите конец среза описания:')
end_slice_of_description = int(6)

with open('categories_dict.json', 'r', encoding='UTF-8') as file:  #открытие json файла и преобразование в словарь питона
    src = file.read()
    new_file = json.loads(src)

worksheet_article = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[0])
worksheet_name = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[1])

new_file['general_menu']['Перчатки'].update({'(Другие) Перчатки': {"Назад в категорию 'Перчатки'": []}})

for i in (1448, 1469, 1470, 1472, 1489, 1508, 1509):
    name = str(worksheet_name[i-2:i-1].values.item())
    article = str(f'{worksheet_article[i-2:i-1].values.item()},000')
    new_file['general_menu']['Перчатки']['(Другие) Перчатки'][name[start_slice_of_name:(- end_slice_of_name)]] = \
        [article, photo, 'Описание: ' + name[:(- end_slice_of_description)],
         'Цена:']

with open('categories_dict.json', 'w', encoding='UTF-8') as file:
    json.dump(new_file, file, indent=4, ensure_ascii=False)
########################################################################################################################