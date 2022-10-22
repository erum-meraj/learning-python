#op from user
op = input("Enter operator")
n1 = float (input("Enter 1st number "))
n2 = float (input("Enter 2nd number "))
if op == '+':
    print ("sum = ", n1+ n2 )
elif op == '-':
    print("diff = ", n1 - n2 )
elif op == '*':
    print("prod = ", n1 * n2 )
elif op == '/':
    print("quot = ", n1 / n2 )
else:
    print("op not defined" )
