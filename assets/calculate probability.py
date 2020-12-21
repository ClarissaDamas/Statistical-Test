#!/usr/bin/env python
# coding: utf-8

# In[3]:


# calculating values
import numpy as np
import pandas as pd

listnumbers = list(map(int, input().split()))
s = pd.Series(listnumbers)
table = s.describe()
print(table)


# calculate z
zlimit = float(input('Which limit?'))


def zformula(n):
    formula = round((s.mean() - n / s.std()), 2)
    return formula


value = zformula(zlimit)
print(value)

# calculate probability
firstdecimal = float(str(value)[:-1])  # understand that
seconddecimal = float(str(value - firstdecimal)[:-2])
print(firstdecimal)
print(seconddecimal)
#Pd_Read_excel = pd.read_excel(r'C:\Users\eeccm\Downloads\Tabela da distribuição normal.xlsx')
mydata = pd.read_excel(r'C:\Users\eeccm\Downloads\Tabela da distribuição normal.xlsx')
print('until here is alright')
print(mydata.info())


# find z
#z = df.at[firstdecimal,seconddecimal]


# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 40 entries, 0 to 39
# Data columns (total 11 columns):
#    Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   Z       40 non-null     float64
#  1   0       40 non-null     float64
#  2   0.01    40 non-null     float64
#  3   0.02    40 non-null     float64
#  4   0.03    40 non-null     float64
#  5   0.04    40 non-null     float64
#  6   0.05    40 non-null     float64
#  7   0.06    40 non-null     float64
#  8   0.07    40 non-null     float64
#  9   0.08    40 non-null     float64
#  10  0.09    40 non-null     float64
# dtypes: float64(11)
# memory usage: 3.6 KB

# ## useful openpyxl
#
# Values only = If you just want the values from a worksheet you can use the Worksheet.values
# open file = The same way as writing, you can use the openpyxl.load_workbook()
#
# need = read file with table,find a way to compare with my z
#        [1.1 find where is the first 2 numbers,compare with first row(do round.number,2)
#        [1.2 find where is the second number,compare with second row(take original number and subtract the nunber on parenteses up here)
#        [return the number that is in the same list as the 1.1 and 1.2
#
#
#
#

# In[ ]:


arraynumbers = np.array(listnumbers)
sortarray_numbers = arraynumbers.sort()
maxarray_numbers = float(arraynumbers.max())
minarray_numbers = float(arraynumbers.min())
averagearray_numbers = float(arraynumbers.mean())
stderray_numbers = float(arraynumbers.std())
multimode_listnumbers = statistics.multimode(listnumbers)
median_listnumbers = float(statistics.median(listnumbers))


# import openpyxl
# wb = openpyxl.load_workbook(r'C:\Users\eeccm\Downloads\Tabela da distribuição normal.xlsx') #use raw string as path
# print(wb.sheetnames)
#
# wss = workbook()
# ws = wss.active
# for row in wb.iter_rows(min_row=1, max_col=3, max_row=2, values_only=True):
#       print(row)
#

# ## useful numpy
# numpy.cumprod = cumulative values
#
# def x < y = True
#
# numpy.cumsum = cumulative values
#
# np.where = Return elements chosen from x or y depending on condition,so i can put I condition on my array based on the N number and apply that is a variable,so use this value for class
#
# for element in b.flat:   =print the numbers from the array without seem as a erray,perfect to put on excell
# ...     print(element)
#
# ndarray.astype = conver the array from one type to another
#
# numpy.mat = turn input into matrix
#
#  vector is an array with a single dimension (there’s no difference between row and column vectors), while a matrix refers to an array with two dimensions. For 3-D or higher dimensional arrays, the term tensor is also commonly used
#
#  an array that contains a range of evenly spaced intervals. To do this, you will specify the first number, last number, and the step size
#
#  You can also use np.linspace() to create an array with values that are spaced linearly in a specified interval = I could use that for the classes
#
#  Working with mathematical formulas = ?
#  Importing and exporting a CSV = ?

# ## todo
#
# find a way to put in excell
# save the file on excell or pc
# think how i wanna it fits in excell
#
# see how i can post on github
#
# find way of doing z and give prob
# find way of doing percent with z and give position
#
# start to think before class how to do hypoteses test
#
