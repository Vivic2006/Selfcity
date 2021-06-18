#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 14 15:48:51 2021

@author: victorbuzy
"""

import os
import xlrd
import numpy as np
import pandas as pd
import shutil



book = xlrd.open_workbook('/Users/victorbuzy/Desktop/projetpython/ScrapingChaudiere/Nomschaudieres2.xls')


sheet = book.sheet_by_index(0)

rows = sheet.nrows
rows = int(rows)


for i in range(0,rows):
    name  = sheet.cell_value(rowx=i, colx=1)
    picture=sheet.cell_value(i,2)
    print(name)
    print(picture)
    filePath = shutil.copy('/Users/victorbuzy/Downloads/'+str(picture), '/Users/victorbuzy/Desktop/projetpython/ScrapingChaudiere/Photosdechaudières2/'+str(name))
    print(filePath)   
    