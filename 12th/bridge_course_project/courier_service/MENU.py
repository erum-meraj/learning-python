print('''WELCOME TO BATMAN COURIER SERVICE:
1.Book courier service
2.View billing details
3.View details of courier delivery boys
4.exit
''')
op= int(input("Enter choice:    "))
if op == 1:
    import book_service
elif op == 2:
    import billing
elif op==3:
    import delivery_det
else:
    print("Thank you :) ")