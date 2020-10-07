import numpy as np
import xlrd

myfile = ("/Users/ahmadli/PycharmProjects/TwitterBot/data.xlsx")

wb = xlrd.open_workbook(myfile)
df = wb.sheet_by_index(0)
df.cell_value(0, 0)

arr = []
for i in range(df.nrows):
    if i == 0 or i == 1: continue
    arr.append(df.cell_value(i, 0) + ".")


def get_post():
    a = np.random.randint(len(arr))
    return (arr[a])

