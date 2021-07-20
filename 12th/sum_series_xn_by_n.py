# sum of series x/1 + x2/2......xn/n
x = float(input("Enter val of x"))
n = int(input("enter no. of terms"))
total = 0
for ctr in range(1, n+1):
    total = total + (x**n)/n
print("Sum = ", total)
