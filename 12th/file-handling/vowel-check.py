#finding vowels in a given file 
def check(stg):
    cnt = 0 
    for i in stg:
        
        if i.capitalize() in ['A', 'I' ,'O', 'U', 'E' ]:
            cnt = cnt + 1
        else:
            continue
    return cnt

#main 
myfiler = open(r"/Users/momeraj/Documents/erum/learning-python-master/12th/file-handling/first-file.txt")
names = myfiler.read()
print("Vowels = ", check(names))
myfiler.close()