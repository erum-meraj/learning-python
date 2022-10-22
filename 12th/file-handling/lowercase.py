#string operation 
def check(text):
    cnt = 0
    print("Lowercase letters: ")
    for i in text:
        if i.islower() == True:
            print(i , end=" ")
            cnt = cnt +1
        else:
            continue
    return cnt

#writing
usertext = open(r"/Users/momeraj/Documents/erum/learning-python-master/12th/file-handling/first-file.txt", "w")
text = input("Enter text: \n")
usertext.write(text)
usertext.close()
#reading
readtext = open(r"/Users/momeraj/Documents/erum/learning-python-master/12th/file-handling/first-file.txt", "r")
rtext = readtext.read()
usertext.close()

#FUNC CALL
count = check(rtext)

#RESULT
print("\nTotal:  ", count)

