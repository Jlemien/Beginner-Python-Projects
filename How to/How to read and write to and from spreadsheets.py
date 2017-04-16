# This is reading from a spreadsheet
# import xlrd
# book=xlrd.open_workbook(r"C:\Users\Josep\Documents\My favorite movies.xlsx")
# print(book.sheet_names())
# first_sheet=book.sheet_by_index(0)
# print(first_sheet.row_values(0))
# column = 0
# row = 6
# cell=first_sheet.cell(row, column)
# print(cell)


# This is writing to a spreadsheet
# import xlwt
# workbook=xlwt.Workbook(encoding="utf")
# sheet1=workbook.add_sheet("Python Sheet1")
# sheet2=workbook.add_sheet("Python Sheet2")
# sheet3=workbook.add_sheet("Python Sheet3")
#
# sheet1.write(0,0,"This is Sheet 1")
# sheet2.write(10,0,"This is Sheet 2")
# sheet3.write(0,10,"This is Sheet 3")
#
# workbook.save("PythonSpreadsheet.xls")
# print("workbook created!")