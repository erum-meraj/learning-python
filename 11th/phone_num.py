#phone number format checker
phone_num = input("Enter phone number (xxx-xxx-xxxx):    ")
if len(phone_num) == 12 and phone_num[3] == '-' and phone_num[7] == '-' :
      
    for a in range(0,len(phone_num)):
        
        if a == 3 or a == 7 or phone_num[a].isdigit() == True:
            if a == (len(phone_num) - 1):
                print(phone_num," is correct")
                break
        else:
            print(phone_num,"is not correct") 
            break
else:
    print(phone_num,"is not correct")