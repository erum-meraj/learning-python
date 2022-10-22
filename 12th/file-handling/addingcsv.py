import csv
from prettytable import PrettyTable
header = ["Sl.no", 'name', 'age']
data = [
    ['1', 'a', '5'],
    ['2', 'a1', '6'],
    ['3', 'a2', '5'],
    ['4', 'a3', '9'],
    ['5', 'a4', '15'],
    ['6', 'a5', '3']
]
file_add = '/Users/momeraj/Documents/erum/learning-python-master/12th/file-handling/test.csv'
with open(file_add, 'w') as csvfile:
    csvw = csv.writer(csvfile)
    csvw.writerow(header)
    csvw.writerows(data)

with open(file_add, 'r') as csvf:
    records = csv.reader(csvf)
    lst = []
    for i in records:
        
        lst.append(i)


    
headers = lst[0]
info = lst[1:]

t = PrettyTable(headers)
t.add_rows(info)
print(t)
