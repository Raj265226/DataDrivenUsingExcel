import openpyxl

path="C:\\Users\Rohit\OneDrive\Desktop\data1.xlsx"

workbook=openpyxl.load_workbook(path)
sheet=workbook.active

for r in range(1,5):
    for c in range(1,5):
        sheet.cell(row=r,column=c).value="welcome"

workbook.save(path)