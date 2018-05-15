import xlsxwriter
import csv

# creating a excel file or spreadsheet file

f = xlsxwriter.Workbook('abc.xlsx')
worksheet = f.add_worksheet()   #adding sheet to the file


worksheet.write('abc.xlsx')

row=1
colum=0
f.close() #c losing the excel file