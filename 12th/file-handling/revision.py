f=open('first-file.txt','wb')
print('Name of the file:',f.name)
f.flush()
f.close()