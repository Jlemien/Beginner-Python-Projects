from xlwt import Workbook

wb = Workbook()
sheet1 = wb.add_sheet("Sheet 1")

wb.save("xlwt example.xls")