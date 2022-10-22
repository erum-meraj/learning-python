#program to perform operations read, write, append on binary file as phone log
import pickle
def write():
    filew = open('log.dat', 'ab')
    record = []
    phone = int(input("ENter phone number:   "))
    name = input("ENter name:   ")
    area_name = input("ENter area name:   ")
    record.append([phone, name , area_name])
    pickle.dump(record, filew)
    filew.close()
    return
def read():
    filer = open('log.dat', 'rb')
    try: 
        while True: 
            data = pickle.load(filer)
            for record in data:
                print('~'*30)
                print("Phone:  ", record[0])
                print("name:  ", record[1])
                print("area name:  ", record[2])
                print('~'*30)
    except:
        print("oops")
    return
def update():
    fileu = open('log.dat', 'rb+')
    phone = int(input("ENter phone number to update:   "))
    try: 
        while True:
            found = False
            pos = fileu.tell()
            record = pickle.load(fileu)
            if record[0][0] == phone:
                fileu.seek(pos)
                record[0][1] = input("ENter name:   ")
                record[0][2] = input("ENter area name:   ")
                pickle.dump(record, fileu)
                found = True
                break
    except:
        if found == False:
            print("No matching record ")
        else:
            print("Record updated")
    return


#main

choice = 1
print('''
OPERATIONS:
1) Write
2) read
3) update
''')

while choice == 1:
    op = int(input("ENter operation number:   "))
    if op == 1:
        write()
    elif op == 2:
        read()
    elif op == 3:
        update()
    else:
        print("invalid option. exiting program")
    choice = int(input("1) another operation \n 2) exit program \n choice =   "))
    
