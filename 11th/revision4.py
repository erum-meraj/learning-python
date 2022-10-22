l1 = eval(input("Enter list"))
l2 = eval(input("Enter seconf list "))
for i in range(len(l1)):
    key = l1[i]
    if key in l2:
        print('overlapped')
        break
else:
    print("seperate")
        
       
