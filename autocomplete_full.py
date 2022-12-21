#import gspread
import pandas as pd
import json

#print('Введите строку начала:')
start_row = 54
#print('Введите строку конца:')
end_row = 60
#print('Введите url картинки:')
photo = 'https://www.sportdepo.ru/upload/iblock/232/2323999d306929be60588acc7e3a7aab.jpeg'
#print('Введите начало среза названия:')
start_slice_of_name = int(6)
#print('Введите конец среза названия:')
end_slice_of_name = int(14)
#print('Введите конец среза описания:')
end_slice_of_description = int(6)

with open('categories_dict.json', 'r', encoding='UTF-8') as file:  #открытие json файла и преобразование в словарь питона
    src = file.read()
    new_file = json.loads(src)

worksheet_article = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[0])
worksheet_name = pd.read_excel('CCM.xlsx', sheet_name='остатки', usecols=[1])

new_file['general_menu']['Аксессуары']['Носки'].update({'Носки Bauer': {"Назад в категорию 'Аксессуары'": []}})
for i in range(start_row, end_row + 1):
    name = str(worksheet_name[i-2:i-1].values.item())
    article = str(f'{worksheet_article[i-2:i-1].values.item()},000')
    new_file['general_menu']['Аксессуары']['Носки']['Носки Bauer'][name[start_slice_of_name:(- end_slice_of_name)]] = \
        [article, photo, 'Описание: ' + name[:(- end_slice_of_description)],
         'Цена:']

with open('categories_dict.json', 'w', encoding='UTF-8') as file:
    json.dump(new_file, file, indent=4, ensure_ascii=False)
########################################################################################################################

