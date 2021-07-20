import math

#menu

print ('''menu
        1. add
        2.sub
        3.mul
        4.div''')

op = int(input("Enter option"))

if op == 1:
    num1 = int(input("Enter first number"))
    num2 = int(input("Enter second number"))
    print ("answer = ", num1+num2)
elif op == 2:
    num1 = int(input("Enter first number"))
    num2 = int(input("Enter secon2nd number"))
    print ("answer = ", num1-num2)
elif op == 3:
    num1 = int(input("Enter first number"))
    num2 = int(input("Enter second number"))
    print ("answer = ", num1*num2)
elif op == 4:
    num1 = int(input("Enter first number"))
    num2 = int(input("Enter second number"))
    print ("answer = ", num1/num2)
else:
    print ("enter valid option")
