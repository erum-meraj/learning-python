import csv
file_add = r'/Users/momeraj/Documents/erum/learning-python-master/12th/file-handling/test_exp.csv'
with open(file_add, 'r') as csvf:
    records = csv.reader(csvf)
    lst = []
    for i in records:
        lst.append(i)

print(records)