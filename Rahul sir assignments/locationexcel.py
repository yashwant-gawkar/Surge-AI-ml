import openpyxl 

wb = openpyxl.Workbook() 

sheet = wb.active 
for i in range(1,101):
    for j in range(1,101):
        c1=sheet.cell(row=i,column=j)
        
        c1.value=str(chr(j+64))+str(i)

wb.save("G:\python\excel.xlsx") 
