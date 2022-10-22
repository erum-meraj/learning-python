import pickle
myfiler = open(r"/Users/momeraj/Documents/erum/learning-python-master/12th/file-handling/output.txt", "wb")

lst = [1,2,3,4,5]
pickle.dump(lst,myfiler)
myfiler.close()

myfile = open(r"/Users/momeraj/Documents/erum/learning-python-master/12th/file-handling/output.txt", "rb")
dat = pickle.load(myfile)
print(dat)
myfiler.close()