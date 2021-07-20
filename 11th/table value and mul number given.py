#table value and multiples given by user
num = int(input("Enter the number     "))
upper_lim = int(input("Enter the number of multiples    "))
for a in range(1, upper_lim+1):
    product = num * a
    print(num, "x", a, "=", product)