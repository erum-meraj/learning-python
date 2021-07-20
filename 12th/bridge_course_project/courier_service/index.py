
import mysql.connector as sql

print('\n\n                 WELCOME TO BATMAN COURIER SERVICE: \n Hi')
print('1.CREATE YOUR COURIER SERVICE ACCOUNT')
print('2.LOGIN')
print('''ENTER 
(1) FOR NEW ACCOUNT 
(2) FOR LOGIN:''')
con = sql.connect(host = 'localhost', user = 'root', password = 'erummeraj', database = 'python_db')
cur = con.cursor()
opt = int(input("Enter choice :      "))
if opt==1:
    uname=input('Enter your username:      ')
    pw=input('Enter your password:      ')
    email=input('Enter your email-id')
    cur.execute("INSERT INTO python_db.courier_service_users (username, u_password , email) VALUES(' "+uname+"', '"+pw+"', '"+email+"')")
    con.commit()
    print('REGISTRATION SUCCESFUL')
    import MENU    
elif opt==2:
    email=input('Enter your email-id')
    pw=input('Enter your PASSWORD:      ')
    import MENU
    
else:
    print("You have exited the platform")