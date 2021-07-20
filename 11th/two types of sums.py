#two types of sums 
num1 = float(input("enter1st number"))
num2 = float(input("enter 2nd number"))
num3 = float(input("enter 3rd number"))

if num1 == num2 or num2 == num3 or num1 == num3:
    print("pls enter 3 distinct numbers ")

else:
    print(num1 + num2 + num3)