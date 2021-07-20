#operator menu
print('''This program can perform the following operations:
      1. Multiplication
      2. division
      3. addition
      4. subtraction''')

#inputs
num1 = float(input("Enter 1st number"))
num2 = float(input("Enter 2nd number"))
op = input("Enter operator (/ * + -)")

#conditions
if op == '+':
    print (num1, "+", num2, "=", num1+num2)
elif op == '-':
    
    print (num1, "-", num2, "=", num1-num2)
elif op == '*':
    ans = num1 * num2
    print (num1, "x", num2, "=", ans)

else:
    ans = num1 / num2
    print (num1, "/", num2, "=", ans)
