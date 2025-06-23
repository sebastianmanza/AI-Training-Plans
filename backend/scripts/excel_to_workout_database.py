import pandas as pd


xlsx = pd.ExcelFile("backend/data/raw/Workouts_to_Database.xlsx")

sheet1 = xlsx.parse(0)

print(sheet1)

#for row in sheet1:
 #   print(row)

