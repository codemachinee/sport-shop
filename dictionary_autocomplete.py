import gspread
import json

print('Введите строку начала:')
start_row = int(input())
print('Введите строку конца:')
end_row = int(input())
print('Введите url картинки:')
photo = str(input())
print('Введите начало среза названия:')
start_slice_of_name = int(input())
print('Введите конец среза названия:')
end_slice_of_name = int(input())
print('Введите конец среза описания:')
end_slice_of_description = int(input())

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

#for i in range(480, 485):
 #   new_file['general_menu']['Защита']['Налокотники']['(EP FT485) Налокотники'] = {worksheet.cell(i, 2).value[12:-14]: [worksheet.cell(i, 1).value, photo, 'Описание: ' + worksheet.cell(i, 2).value[:-6], 'Цена:']}
#with open('new.json', 'w') as file:
 #   json.dump(new_file, file, indent=4, ensure_ascii=False)
