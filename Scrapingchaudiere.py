

import os
import xlrd
import numpy as np
import pandas as pd



book = xlrd.open_workbook('/Users/victorbuzy/Desktop/projetpython/ScrapingChaudiere/Nomschaudieres2.xls')


sheet = book.sheet_by_index(0)

rows = sheet.nrows
cols = sheet.ncols
rows = int(rows)
print(rows)




myFileName = '/Users/victorbuzy/Desktop/projetpython/ScrapingChaudiere/Photosdechaudières2/'
# load the workbook, and put the sheet into a variable


for i in range(0,rows):
    name  = sheet.cell_value(rowx=i, colx=1)
    print(name)
    os.mkdir(myFileName +str(name))




