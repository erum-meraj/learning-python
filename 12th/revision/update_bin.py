#updating a binary file

import pickle
import os

def write():
    f = open('phone.dat', 'ab')
    record = []
    pno = int(input("Enter phone number:   "))
    name = input("Enter name:   ")
    aname = input("Enter area name:   ")
    record.append([pno, name, aname])
    pickle.dump(record,f)
    f.close()

def read():
    file = open('phone.dat', 'rb')

    try:
        while True:
            data = pickle.load(file)
            for record in data:
                print("phone:  ", record[0])
                print("name:  ", record[1])
                print("area name:  ", record[2])
    except EOFError:
        file.close()

def update():
    file = open('phone.dat', 'rb')
    temp_file = open('temp.dat', 'wb')
    found = 0
    pnum = int(input("Phone number to be updated"))
    while True:
        try:
            data = pickle.load(file)
            for record in data:
                if record[0] == pnum:
                    record[1] = input("Enter name")
                    record[2] = input("Enter area name")
                    pickle.dump(data, temp_file)
                    found = 1
                else:
                    pickle.dump(data, temp_file)
        except EOFError:
            break
    file.close()
    temp_file.close()
    if found == 0:
        print("No matching record found ")
    else:
        print("Record updated :) ")
    os.remove('phone.dat')
    os.rename('temp.dat', 'phone.dat')
                    
#main
choice = 1
while choice == 1:
    print("OPERATIONS \n 1) write record \n 2) read record \n 3) update record ")
    op = int(input("Enter operation number:  "))
    if op ==1:
        write()
    elif op == 2:
        read()
    elif op == 3:
        update()
    else:
        print("Invalid option")
        break
    choice = int(input("Enter 1 to perform another operation (0 to exit):   "))
