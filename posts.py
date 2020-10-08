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
    while True:
        index = np.random.randint(len(arr))
        get_tweet = arr[index]
        if len(get_tweet) > 280:
            continue
        else:
            return get_tweet

