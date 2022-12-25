#import gspread
import pandas as pd
import json

#print('Введите строку начала:')
start_row = 999
#print('Введите строку конца:')
end_row = 1016
#print('Введите url картинки:')
photo = 'https://static.insales-cdn.com/images/products/1/6291/392116371/import_files_e1_e13a2343129111ebaee0704d7b8986a2_ec4f8b88129111ebaee0704d7b8986a2.jpg'
#print('Введите начало среза названия:')
start_slice_of_name = int(17)
#print('Введите конец среза названия:')
end_slice_of_name = int(16)
#print('Введите конец среза описания:')
end_slice_of_description = int(6)

with open('categories_dict.json', 'r', encoding='UTF-8') as file:  #открытие json файла и преобразование в словарь питона
    src = file.read()
    new_file = json.loads(src)

worksheet_article = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[0])
worksheet_name = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[1])

new_file['general_menu']['Коньки'].update({'(9350) Коньки': {"Назад в категорию 'Коньки'": []}})

for i in range(start_row, end_row + 1):
    name = str(worksheet_name[i-2:i-1].values.item())
    article = str(f'{worksheet_article[i-2:i-1].values.item()},000')
    new_file['general_menu']['Коньки']['(9350) Коньки'][name[start_slice_of_name:(- end_slice_of_name)]] = \
        [article, photo, 'Описание: ' + name[:(- end_slice_of_description)],
         'Цена:']

with open('categories_dict.json', 'w', encoding='UTF-8') as file:
    json.dump(new_file, file, indent=4, ensure_ascii=False)
########################################################################################################################

#print('Введите строку начала:')
start_row = 1018
#print('Введите строку конца:')
end_row = 1023
#print('Введите url картинки:')
photo = 'https://hockeyclub.ru/upload/resize_cache/iblock/076/1000_1000_1/IMG_7439.jpg'
#print('Введите начало среза названия:')
start_slice_of_name = int(17)
#print('Введите конец среза названия:')
end_slice_of_name = int(16)
#print('Введите конец среза описания:')
end_slice_of_description = int(6)

with open('categories_dict.json', 'r', encoding='UTF-8') as file:  #открытие json файла и преобразование в словарь питона
    src = file.read()
    new_file = json.loads(src)

worksheet_article = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[0])
worksheet_name = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[1])

new_file['general_menu']['Коньки'].update({'(9360) Коньки': {"Назад в категорию 'Коньки'": []}})

for i in range(start_row, end_row + 1):
    name = str(worksheet_name[i-2:i-1].values.item())
    article = str(f'{worksheet_article[i-2:i-1].values.item()},000')
    new_file['general_menu']['Коньки']['(9360) Коньки'][name[start_slice_of_name:(- end_slice_of_name)]] = \
        [article, photo, 'Описание: ' + name[:(- end_slice_of_description)],
         'Цена:']

with open('categories_dict.json', 'w', encoding='UTF-8') as file:
    json.dump(new_file, file, indent=4, ensure_ascii=False)
########################################################################################################################

#print('Введите строку начала:')
start_row = 1025
#print('Введите строку конца:')
end_row = 1041
#print('Введите url картинки:')
photo = 'https://wintermax.ru/upload/iblock/f93/f93ad7b129e7eedb86b873cc687d7028.png'
#print('Введите начало среза названия:')
start_slice_of_name = int(17)
#print('Введите конец среза названия:')
end_slice_of_name = int(16)
#print('Введите конец среза описания:')
end_slice_of_description = int(6)

with open('categories_dict.json', 'r', encoding='UTF-8') as file:  #открытие json файла и преобразование в словарь питона
    src = file.read()
    new_file = json.loads(src)

worksheet_article = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[0])
worksheet_name = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[1])

new_file['general_menu']['Коньки'].update({'(9370) Коньки': {"Назад в категорию 'Коньки'": []}})

for i in range(start_row, end_row + 1):
    name = str(worksheet_name[i-2:i-1].values.item())
    article = str(f'{worksheet_article[i-2:i-1].values.item()},000')
    new_file['general_menu']['Коньки']['(9370) Коньки'][name[start_slice_of_name:(- end_slice_of_name)]] = \
        [article, photo, 'Описание: ' + name[:(- end_slice_of_description)],
         'Цена:']

with open('categories_dict.json', 'w', encoding='UTF-8') as file:
    json.dump(new_file, file, indent=4, ensure_ascii=False)
########################################################################################################################

#print('Введите строку начала:')
start_row = 1043
#print('Введите строку конца:')
end_row = 1046
#print('Введите url картинки:')
photo = 'https://ccm.ru/upload/iblock/65b/Super-Tacks-9380-Senior-Goalie-Skates-6.png'
#print('Введите начало среза названия:')
start_slice_of_name = int(0)
#print('Введите конец среза названия:')
end_slice_of_name = int(8)
#print('Введите конец среза описания:')
end_slice_of_description = int(6)

with open('categories_dict.json', 'r', encoding='UTF-8') as file:  #открытие json файла и преобразование в словарь питона
    src = file.read()
    new_file = json.loads(src)

worksheet_article = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[0])
worksheet_name = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[1])

new_file['general_menu']['Коньки'].update({'(9380) Коньки': {"Назад в категорию 'Коньки'": []}})

for i in range(start_row, end_row + 1):
    name = str(worksheet_name[i-2:i-1].values.item())
    article = str(f'{worksheet_article[i-2:i-1].values.item()},000')
    new_file['general_menu']['Коньки']['(9380) Коньки'][name[start_slice_of_name:(- end_slice_of_name)]] = \
        [article, photo, 'Описание: ' + name[:(- end_slice_of_description)],
         'Цена:']

with open('categories_dict.json', 'w', encoding='UTF-8') as file:
    json.dump(new_file, file, indent=4, ensure_ascii=False)
########################################################################################################################

#print('Введите строку начала:')
start_row = 1065
#print('Введите строку конца:')
end_row = 1074
#print('Введите url картинки:')
photo = 'https://one-of-sport.ru/images/watermarked/1/detailed/54/9ded34b3-4c97-11ea-aac5-00155d031309_f1f90eb3-0244-11eb-88c8-00155d031309.jpeg'
#print('Введите начало среза названия:')
start_slice_of_name = int(17)
#print('Введите конец среза названия:')
end_slice_of_name = int(16)
#print('Введите конец среза описания:')
end_slice_of_description = int(6)

with open('categories_dict.json', 'r', encoding='UTF-8') as file:  #открытие json файла и преобразование в словарь питона
    src = file.read()
    new_file = json.loads(src)

worksheet_article = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[0])
worksheet_name = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[1])

new_file['general_menu']['Коньки'].update({'(AS3) Коньки': {"Назад в категорию 'Коньки'": []}})

for i in range(start_row, end_row + 1):
    name = str(worksheet_name[i-2:i-1].values.item())
    article = str(f'{worksheet_article[i-2:i-1].values.item()},000')
    new_file['general_menu']['Коньки']['(AS3) Коньки'][name[start_slice_of_name:(- end_slice_of_name)]] = \
        [article, photo, 'Описание: ' + name[:(- end_slice_of_description)],
         'Цена:']

with open('categories_dict.json', 'w', encoding='UTF-8') as file:
    json.dump(new_file, file, indent=4, ensure_ascii=False)
########################################################################################################################

#print('Введите строку начала:')
start_row = 1076
#print('Введите строку конца:')
end_row = 1085
#print('Введите url картинки:')
photo = 'https://ccm.ru/upload/iblock/e20/AS3-Pro-Senior-Goalie-Skates-3.png'
#print('Введите начало среза названия:')
start_slice_of_name = int(17)
#print('Введите конец среза названия:')
end_slice_of_name = int(16)
#print('Введите конец среза описания:')
end_slice_of_description = int(6)

with open('categories_dict.json', 'r', encoding='UTF-8') as file:  #открытие json файла и преобразование в словарь питона
    src = file.read()
    new_file = json.loads(src)

worksheet_article = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[0])
worksheet_name = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[1])

new_file['general_menu']['Коньки'].update({'(AS3 PRO) Коньки': {"Назад в категорию 'Коньки'": []}})

for i in range(start_row, end_row + 1):
    name = str(worksheet_name[i-2:i-1].values.item())
    article = str(f'{worksheet_article[i-2:i-1].values.item()},000')
    new_file['general_menu']['Коньки']['(AS3 PRO) Коньки'][name[start_slice_of_name:(- end_slice_of_name)]] = \
        [article, photo, 'Описание: ' + name[:(- end_slice_of_description)],
         'Цена:']

with open('categories_dict.json', 'w', encoding='UTF-8') as file:
    json.dump(new_file, file, indent=4, ensure_ascii=False)
########################################################################################################################
#print('Введите строку начала:')
start_row = 1087
#print('Введите строку конца:')
end_row = 1099
#print('Введите url картинки:')
photo = 'https://drive.google.com/file/d/1PQk9qBGAubAhc_eC3aCvvAE4rr4zHkoe/view?usp=share_link'
#print('Введите начало среза названия:')
start_slice_of_name = int(0)
#print('Введите конец среза названия:')
end_slice_of_name = int(6)
#print('Введите конец среза описания:')
end_slice_of_description = int(6)

with open('categories_dict.json', 'r', encoding='UTF-8') as file:  #открытие json файла и преобразование в словарь питона
    src = file.read()
    new_file = json.loads(src)

worksheet_article = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[0])
worksheet_name = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[1])

new_file['general_menu']['Коньки'].update({'(BAUER) Коньки': {"Назад в категорию 'Коньки'": []}})

for i in range(start_row, end_row + 1):
    name = str(worksheet_name[i-2:i-1].values.item())
    article = str(f'{worksheet_article[i-2:i-1].values.item()},000')
    new_file['general_menu']['Коньки']['(BAUER) Коньки'][name[start_slice_of_name:(- end_slice_of_name)]] = \
        [article, photo, 'Описание: ' + name[:(- end_slice_of_description)],
         'Цена:']

with open('categories_dict.json', 'w', encoding='UTF-8') as file:
    json.dump(new_file, file, indent=4, ensure_ascii=False)
########################################################################################################################
#print('Введите строку начала:')
start_row = 1101
#print('Введите строку конца:')
end_row = 1110
#print('Введите url картинки:')
photo = 'https://reeform.ru/wa-data/public/shop/products/62/43/14362/images/2910/2910.750x0.jpg'
#print('Введите начало среза названия:')
start_slice_of_name = int(17)
#print('Введите конец среза названия:')
end_slice_of_name = int(16)
#print('Введите конец среза описания:')
end_slice_of_description = int(6)

with open('categories_dict.json', 'r', encoding='UTF-8') as file:  #открытие json файла и преобразование в словарь питона
    src = file.read()
    new_file = json.loads(src)

worksheet_article = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[0])
worksheet_name = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[1])

new_file['general_menu']['Коньки'].update({'(FT2) Коньки': {"Назад в категорию 'Коньки'": []}})

for i in range(start_row, end_row + 1):
    name = str(worksheet_name[i-2:i-1].values.item())
    article = str(f'{worksheet_article[i-2:i-1].values.item()},000')
    new_file['general_menu']['Коньки']['(FT2) Коньки'][name[start_slice_of_name:(- end_slice_of_name)]] = \
        [article, photo, 'Описание: ' + name[:(- end_slice_of_description)],
         'Цена:']

with open('categories_dict.json', 'w', encoding='UTF-8') as file:
    json.dump(new_file, file, indent=4, ensure_ascii=False)
########################################################################################################################

#print('Введите строку начала:')
start_row = 1112
#print('Введите строку конца:')
end_row = 1123
#print('Введите url картинки:')
photo = 'https://ccm.ru/upload/iblock/7cf/m15d2r5y4kezp1uoc5xiigwuac9z1ky7/Jetspeed-FT460-Junior-1.png'
#print('Введите начало среза названия:')
start_slice_of_name = int(17)
#print('Введите конец среза названия:')
end_slice_of_name = int(16)
#print('Введите конец среза описания:')
end_slice_of_description = int(6)

with open('categories_dict.json', 'r', encoding='UTF-8') as file:  #открытие json файла и преобразование в словарь питона
    src = file.read()
    new_file = json.loads(src)

worksheet_article = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[0])
worksheet_name = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[1])

new_file['general_menu']['Коньки'].update({'(FT460) Коньки': {"Назад в категорию 'Коньки'": []}})

for i in range(start_row, end_row + 1):
    name = str(worksheet_name[i-2:i-1].values.item())
    article = str(f'{worksheet_article[i-2:i-1].values.item()},000')
    new_file['general_menu']['Коньки']['(FT460) Коньки'][name[start_slice_of_name:(- end_slice_of_name)]] = \
        [article, photo, 'Описание: ' + name[:(- end_slice_of_description)],
         'Цена:']

with open('categories_dict.json', 'w', encoding='UTF-8') as file:
    json.dump(new_file, file, indent=4, ensure_ascii=False)
########################################################################################################################

#print('Введите строку начала:')
start_row = 1127
#print('Введите строку конца:')
end_row = 1133
#print('Введите url картинки:')
photo = 'https://ccm.ru/upload/iblock/0db/CCM-Jetspeed-FT475-Junior-Ice-Hockey-Skates-5.jpg'
#print('Введите начало среза названия:')
start_slice_of_name = int(17)
#print('Введите конец среза названия:')
end_slice_of_name = int(14)
#print('Введите конец среза описания:')
end_slice_of_description = int(6)

with open('categories_dict.json', 'r', encoding='UTF-8') as file:  #открытие json файла и преобразование в словарь питона
    src = file.read()
    new_file = json.loads(src)

worksheet_article = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[0])
worksheet_name = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[1])

new_file['general_menu']['Коньки'].update({'(FT475) Коньки': {"Назад в категорию 'Коньки'": []}})

for i in range(start_row, end_row + 1):
    name = str(worksheet_name[i-2:i-1].values.item())
    article = str(f'{worksheet_article[i-2:i-1].values.item()},000')
    new_file['general_menu']['Коньки']['(FT475) Коньки'][name[start_slice_of_name:(- end_slice_of_name)]] = \
        [article, photo, 'Описание: ' + name[:(- end_slice_of_description)],
         'Цена:']

with open('categories_dict.json', 'w', encoding='UTF-8') as file:
    json.dump(new_file, file, indent=4, ensure_ascii=False)
########################################################################################################################

#print('Введите строку начала:')
start_row = 1139
#print('Введите строку конца:')
end_row = 1167
#print('Введите url картинки:')
photo = 'https://glav-sport.ru/images/stories/virtuemart/product/коньки%20CCM%20JetSpeed%20FT4%20Sr_61.png'
#print('Введите начало среза названия:')
start_slice_of_name = int(17)
#print('Введите конец среза названия:')
end_slice_of_name = int(14)
#print('Введите конец среза описания:')
end_slice_of_description = int(6)

with open('categories_dict.json', 'r', encoding='UTF-8') as file:  #открытие json файла и преобразование в словарь питона
    src = file.read()
    new_file = json.loads(src)

worksheet_article = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[0])
worksheet_name = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[1])

new_file['general_menu']['Коньки'].update({'(SK FT4) Коньки': {"Назад в категорию 'Коньки'": []}})

for i in range(start_row, end_row + 1):
    name = str(worksheet_name[i-2:i-1].values.item())
    article = str(f'{worksheet_article[i-2:i-1].values.item()},000')
    new_file['general_menu']['Коньки']['(SK FT4) Коньки'][name[start_slice_of_name:(- end_slice_of_name)]] = \
        [article, photo, 'Описание: ' + name[:(- end_slice_of_description)],
         'Цена:']

with open('categories_dict.json', 'w', encoding='UTF-8') as file:
    json.dump(new_file, file, indent=4, ensure_ascii=False)
########################################################################################################################

#print('Введите строку начала:')
start_row = 1169
#print('Введите строку конца:')
end_row = 1186
#print('Введите url картинки:')
photo = 'https://hockeymall.ru/wa-data/public/shop/products/69/50/5069/images/32086/32086.750x0.jpg'
#print('Введите начало среза названия:')
start_slice_of_name = int(17)
#print('Введите конец среза названия:')
end_slice_of_name = int(14)
#print('Введите конец среза описания:')
end_slice_of_description = int(6)

with open('categories_dict.json', 'r', encoding='UTF-8') as file:  #открытие json файла и преобразование в словарь питона
    src = file.read()
    new_file = json.loads(src)

worksheet_article = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[0])
worksheet_name = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[1])

new_file['general_menu']['Коньки'].update({'(SK FT4PRO) Коньки': {"Назад в категорию 'Коньки'": []}})

for i in range(start_row, end_row + 1):
    name = str(worksheet_name[i-2:i-1].values.item())
    article = str(f'{worksheet_article[i-2:i-1].values.item()},000')
    new_file['general_menu']['Коньки']['(SK FT4PRO) Коньки'][name[start_slice_of_name:(- end_slice_of_name)]] = \
        [article, photo, 'Описание: ' + name[:(- end_slice_of_description)],
         'Цена:']

with open('categories_dict.json', 'w', encoding='UTF-8') as file:
    json.dump(new_file, file, indent=4, ensure_ascii=False)
########################################################################################################################

#print('Введите строку начала:')
start_row = 1188
#print('Введите строку конца:')
end_row = 1201
#print('Введите url картинки:')
photo = 'https://ccm.ru/upload/iblock/b35/qc2uwhzrjxf61buisjtn9sepdzn2wmw1/CCM-Ribcor-100K-Pro-Senior-Ice-Hockey-Skates.jpg'
#print('Введите начало среза названия:')
start_slice_of_name = int(17)
#print('Введите конец среза названия:')
end_slice_of_name = int(14)
#print('Введите конец среза описания:')
end_slice_of_description = int(6)

with open('categories_dict.json', 'r', encoding='UTF-8') as file:  #открытие json файла и преобразование в словарь питона
    src = file.read()
    new_file = json.loads(src)

worksheet_article = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[0])
worksheet_name = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[1])

new_file['general_menu']['Коньки'].update({'(SK RIB 100K PRO) Коньки': {"Назад в категорию 'Коньки'": []}})

for i in range(start_row, end_row + 1):
    name = str(worksheet_name[i-2:i-1].values.item())
    article = str(f'{worksheet_article[i-2:i-1].values.item()},000')
    new_file['general_menu']['Коньки']['(SK RIB 100K PRO) Коньки'][name[start_slice_of_name:(- end_slice_of_name)]] = \
        [article, photo, 'Описание: ' + name[:(- end_slice_of_description)],
         'Цена:']

with open('categories_dict.json', 'w', encoding='UTF-8') as file:
    json.dump(new_file, file, indent=4, ensure_ascii=False)
########################################################################################################################

#print('Введите строку начала:')
start_row = 1203
#print('Введите строку конца:')
end_row = 1214
#print('Введите url картинки:')
photo = 'https://hockey-overtime.ru/upload/iblock/40c/40ceb439cfebbd167e59b7a4baab09ed.jpg'
#print('Введите начало среза названия:')
start_slice_of_name = int(17)
#print('Введите конец среза названия:')
end_slice_of_name = int(14)
#print('Введите конец среза описания:')
end_slice_of_description = int(6)

with open('categories_dict.json', 'r', encoding='UTF-8') as file:  #открытие json файла и преобразование в словарь питона
    src = file.read()
    new_file = json.loads(src)

worksheet_article = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[0])
worksheet_name = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[1])

new_file['general_menu']['Коньки'].update({'(SK RIB 86K) Коньки': {"Назад в категорию 'Коньки'": []}})

for i in range(start_row, end_row + 1):
    name = str(worksheet_name[i-2:i-1].values.item())
    article = str(f'{worksheet_article[i-2:i-1].values.item()},000')
    new_file['general_menu']['Коньки']['(SK RIB 86K) Коньки'][name[start_slice_of_name:(- end_slice_of_name)]] = \
        [article, photo, 'Описание: ' + name[:(- end_slice_of_description)],
         'Цена:']

with open('categories_dict.json', 'w', encoding='UTF-8') as file:
    json.dump(new_file, file, indent=4, ensure_ascii=False)
########################################################################################################################

#print('Введите строку начала:')
start_row = 1216
#print('Введите строку конца:')
end_row = 1226
#print('Введите url картинки:')
photo = 'https://hockey-overtime.ru/upload/iblock/40c/40ceb439cfebbd167e59b7a4baab09ed.jpg'
#print('Введите начало среза названия:')
start_slice_of_name = int(17)
#print('Введите конец среза названия:')
end_slice_of_name = int(14)
#print('Введите конец среза описания:')
end_slice_of_description = int(6)

with open('categories_dict.json', 'r', encoding='UTF-8') as file:  #открытие json файла и преобразование в словарь питона
    src = file.read()
    new_file = json.loads(src)

worksheet_article = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[0])
worksheet_name = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[1])

new_file['general_menu']['Коньки'].update({'(SK RIB 90K) Коньки': {"Назад в категорию 'Коньки'": []}})

for i in range(start_row, end_row + 1):
    name = str(worksheet_name[i-2:i-1].values.item())
    article = str(f'{worksheet_article[i-2:i-1].values.item()},000')
    new_file['general_menu']['Коньки']['(SK RIB 90K) Коньки'][name[start_slice_of_name:(- end_slice_of_name)]] = \
        [article, photo, 'Описание: ' + name[:(- end_slice_of_description)],
         'Цена:']

with open('categories_dict.json', 'w', encoding='UTF-8') as file:
    json.dump(new_file, file, indent=4, ensure_ascii=False)
########################################################################################################################

#print('Введите строку начала:')
#start_row = 1216
#print('Введите строку конца:')
#end_row = 1226
#print('Введите url картинки:')
photo = 'https://ccm.ru/upload/iblock/65b/Super-Tacks-9380-Senior-Goalie-Skates-6.png'
#print('Введите начало среза названия:')
start_slice_of_name = int(15)
#print('Введите конец среза названия:')
end_slice_of_name = int(16)
#print('Введите конец среза описания:')
end_slice_of_description = int(6)

with open('categories_dict.json', 'r', encoding='UTF-8') as file:  #открытие json файла и преобразование в словарь питона
    src = file.read()
    new_file = json.loads(src)

worksheet_article = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[0])
worksheet_name = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[1])

new_file['general_menu']['Коньки'].update({'(Вратарские) Коньки': {"Назад в категорию 'Коньки'": []}})

for i in (1229, 1230, 1232, 1233, 1234):
    name = str(worksheet_name[i-2:i-1].values.item())
    article = str(f'{worksheet_article[i-2:i-1].values.item()},000')
    new_file['general_menu']['Коньки']['(Вратарские) Коньки'][name[start_slice_of_name:(- end_slice_of_name)]] = \
        [article, photo, 'Описание: ' + name[:(- end_slice_of_description)],
         'Цена:']

with open('categories_dict.json', 'w', encoding='UTF-8') as file:
    json.dump(new_file, file, indent=4, ensure_ascii=False)
########################################################################################################################

#print('Введите строку начала:')
start_row = 1236
#print('Введите строку конца:')
end_row = 1239
#print('Введите url картинки:')
photo = 'https://ccm.ru/upload/iblock/367/SK-CCM-Pirouette.png'
#print('Введите начало среза названия:')
start_slice_of_name = int(16)
#print('Введите конец среза названия:')
end_slice_of_name = int(13)
#print('Введите конец среза описания:')
end_slice_of_description = int(6)

with open('categories_dict.json', 'r', encoding='UTF-8') as file:  #открытие json файла и преобразование в словарь питона
    src = file.read()
    new_file = json.loads(src)

worksheet_article = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[0])
worksheet_name = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[1])

new_file['general_menu']['Коньки'].update({'(Фигурные) Коньки': {"Назад в категорию 'Коньки'": []}})

for i in range(start_row, end_row + 1):
    name = str(worksheet_name[i-2:i-1].values.item())
    article = str(f'{worksheet_article[i-2:i-1].values.item()},000')
    new_file['general_menu']['Коньки']['(Фигурные) Коньки'][name[start_slice_of_name:(- end_slice_of_name)]] = \
        [article, photo, 'Описание: ' + name[:(- end_slice_of_description)],
         'Цена:']

with open('categories_dict.json', 'w', encoding='UTF-8') as file:
    json.dump(new_file, file, indent=4, ensure_ascii=False)
################################################################################################################

#print('Введите строку начала:')
#start_row = 1236
#print('Введите строку конца:')
#end_row = 1239
#print('Введите url картинки:')
photo = 'https://drive.google.com/file/d/1PQk9qBGAubAhc_eC3aCvvAE4rr4zHkoe/view?usp=share_link'
#print('Введите начало среза названия:')
start_slice_of_name = int(7)
#print('Введите конец среза названия:')
end_slice_of_name = int(13)
#print('Введите конец среза описания:')
end_slice_of_description = int(6)

with open('categories_dict.json', 'r', encoding='UTF-8') as file:  #открытие json файла и преобразование в словарь питона
    src = file.read()
    new_file = json.loads(src)

worksheet_article = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[0])
worksheet_name = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[1])

new_file['general_menu']['Коньки'].update({'(Другие) Коньки': {"Назад в категорию 'Коньки'": []}})

for i in (995, 997, 1048, 1049, 1051, 1052, 1054, 1055, 1057, 1058, 1060, 1062, 1063, 1125, 1135, 1137):
    name = str(worksheet_name[i-2:i-1].values.item())
    article = str(f'{worksheet_article[i-2:i-1].values.item()},000')
    new_file['general_menu']['Коньки']['(Другие) Коньки'][name[start_slice_of_name:(- end_slice_of_name)]] = \
        [article, photo, 'Описание: ' + name[:(- end_slice_of_description)],
         'Цена:']

with open('categories_dict.json', 'w', encoding='UTF-8') as file:
    json.dump(new_file, file, indent=4, ensure_ascii=False)
################################################################################################################