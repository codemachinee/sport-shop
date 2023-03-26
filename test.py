from openpyxl import load_workbook

wb = load_workbook('CCM.xlsx')
ws = wb['кэш']
for i in range(1, ws.max_row + 1):
    if ws.cell(i, 1).value == 127154290:
        ws.cell(i, 6).value = 89266407768
        break
wb.save('CCM.xlsx')
#ws.insert_rows(1)
#ws['A1'] = 3
#ws['B1'] = 3
#ws['C1'] = 3
#wb.save('CCM.xlsx')
#for row in ws['A1':'A10']:
 #   for cell in row:
  #      if str(cell.value) == str(214):
  #          print('Yes')
  #          break
            #ws.delete_rows(cell.row)
  #      break
       #wb.save('CCM.xlsx')
#ws.delete_rows(1, 2)
#ws.append(['Семен', 123, 124.11])
#wb.save('CCM.xlsx')