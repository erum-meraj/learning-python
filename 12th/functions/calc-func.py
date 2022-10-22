#input operator 

#func
def calc(n1, n2, op):
    if op == '+':
        ans = n1+n2
        print("Answer: ", ans)
    elif op == '-':
        ans = n1-n2
        print("Answer: ", ans)
    elif op == '*':
        ans = n1*n2
        print("Answer: ", ans)
    elif op == '/':
        ans = n1/n2
        print("Answer: ", ans)
    else:
        print("operator not defined")

#_main_
num1 = float(input("Enter 1st number:   "))
num2 = float(input("Enter 2nd number:   "))
print('''OPERATIONS: 
1. Addition (+)
2. subtraction (-)
3. multiplication (*)
4. division (/) ''')
opr = input("Enter operator: ")
calc(num1, num2, opr)