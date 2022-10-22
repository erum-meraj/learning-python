
def accept_data():
    n = 1
    while n != 0:
        data = open(r"/Users/momeraj/Documents/erum/learning-python-master/12th/file-handling/student_data.txt", "a")
        std_name = input("Enter name:   ")
        std_roll= input("Enter roll number:   ")
        record = std_roll+"        "+ std_name+"\n"
        data.write(record)
        data.close()
        n = int(input('''Enter 0 -> exit\nEnter 1 -> enter another record \n'''))
    return

def  read_data():
    data = open(r"/Users/momeraj/Documents/erum/learning-python-master/12th/file-handling/student_data.txt", "r")
    print("Name    Roll no.")
    for i in range(1, 7):
        records = data.readline()
        print(records)
    data.close()
    return

#_main_
print('''OPTIONS:
1. Write data in file 
2. Read data from file''' )
op = int(input("Enter choice:  "))

if op == 1:
    accept_data()
    print("Records added")

else:
    read_data()