import mysql.connector as  sql
con=sql.connect(host= 'localhost' ,user= 'root' ,passwd= 'erummeraj', database='python_db' )
cur=con.cursor()

print('''\n\n         ORDER PLACEMENT AND DETAILS
A.courier placement
B.courier order details''')
sect=str(input('enter the section that you want to access:'))
if sect=="A":
    print('COURIER-ORDER')
    uname = input("Enter username:   ")
    phone = input("Enter your phone number:   ")
    email = input("Enter your e-mail id:   ")
    address = input("Enter your address:   ")
    dest=(input('enter the receiver address:'))
    cur.execute("INSERT INTO python_db.orders (u_name, p_number , email, address, destination) VALUES(' "+uname+"', '"+phone+"', '"+email+"', '"+address+"', '"+dest+"')")
    con.commit()
    print(" \n\n")
elif sect=="B":
    S = input('do you want to see your courier order details''(yes.../..no):')
    if S=="yes":
        a=input('enter the customer mob number:')
    else:
        print('Thank you')
