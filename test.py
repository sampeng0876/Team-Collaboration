from openpyxl import Workbook

data_list = ['', 'EMCU8377066', '143357136749', '', 'DEPARTED', 'EGL', 'EVER LASTING', '05/10/23 08:00', '05/11/23 14:16', 'COMMUNITY - OUT', 'RELEASED', 'RELEASED', '', '', '', '40/GP/96', '28065.0', '', '05/16/23 08:00', '05/16/23 10:52', '']

workbook = Workbook()
sheet = workbook.active

row = 1
column = 1
print(data_list)
for item in data_list:
    sheet.cell(row=row, column=column).value = item
    column += 1

    if column % 4 == 0:
        row += 1
        column = 1

workbook.save('data.xlsx')

print('Done')
