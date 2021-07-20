import pickle
import pyperclip

dictionary = {}

with open("Your Path\\pass_sys.txt", "br") as readfile:
    dictionary = pickle.load(readfile)

email = input("Enter your User ID : ")
if "1" in email:
    email1 = input("Enter your User ID : ")
    with open("Myproj\\project2\\proj1.txt", "w") as f:
        store_email = f.write(email1)

        password= input("Enter your password : ")
        with open("Myproj\\project2\\password.txt", "w") as a:
            store_pas = a.write(password)

with open("Your Path\\proj1.txt", "r") as fr:
    check_email = fr.read()
        
if email == check_email:
    password2 = input("Enter your password : ")
    with open("Your Path\\password.txt", "r") as ar:
        check_pas = ar.read()
    if password2 == check_pas:
        head = input("To know your saved password press '1' to save password press '2' : ")
        if "2" in head:
            account = input("Enter your account name : ").lower()
            password = input("Enter your password : ")

            conf = input("Would you like to save it (y/n) : ")

            if "y" in conf:
                dictionary[account] = password

                with open("Your Path\\pass_sys.txt", "bw") as filewrite:
                    dictionary = pickle.dump(dictionary, filewrite, protocol=2)
                print(f"Done! Your {account}'s password has been saved")

            else:
                print("Ok, your data is not saved....")
    
    
        if "1" in head:
            know_acc = input("Which account's password you want to know? : ").lower()
            with open("Your Path\\pass_sys.txt", "br") as readfile:
                dictionary = pickle.load(readfile)
                
            if know_acc in dictionary:
                password3 = print("Your password is ", dictionary[know_acc] ,"\nYour password has been copied to your clipboard")
                pyperclip.copy(dictionary[know_acc])
            
            else:
                print("Invalid account name. These passsword has not been saved")

input()
