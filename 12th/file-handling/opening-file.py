#entering data in the file
myfilew = open(r"/Users/momeraj/Documents/erum/learning-python-master/12th/file-handling/first-file.txt", "w")
for i in range(5):
    name = input("Enter name:   ")
    myfilew.write(name)
    myfilew.write("\n")
myfilew.close()
#reading data from a file 
myfiler = open(r"/Users/momeraj/Documents/erum/learning-python-master/12th/file-handling/first-file.txt", "r")
for i in range(5):
    names = myfiler.readline()
    print(names)
myfiler.close()
    