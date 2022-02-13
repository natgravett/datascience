import openpyxl
import os
os.getcwd()

import pandas as pd
file = '801_Edgbaston.xlsx'
data = pd.ExcelFile(file)
print(data.sheet_names) #this returns the all the sheets in the excel file
['Site_1']

df = data.parse('Site_1')
df.info
df.head(10)

ps = openpyxl.load_workbook('801_Edgbaston.xlsx')
sheet = ps['Site_1']
sheet.max_row
