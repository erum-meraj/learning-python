n = int(input("Enter no. of numbers "))
m = int(input("Enter divisor "))
print("numbers which r divisible by ", m, ": ")
for ctr in range (1, n + 1):
    if ctr % m == 0:
        print(ctr, end = "  ")
        if ctr%2 == 0:
            print ("Even")
        else:
            print("odd")
'''
while loop
n = int(input("Enter no. of numbers "))
m = int(input("Enter divisor "))
print("numbers which r divisible by ", m, ": ")
ctr = 1
while ctr <= n:
    if ctr % m == 0:
        print(ctr, end = "  ")
        if ctr%2 == 0:
            print ("Even")
        else:
            print("odd")
    ctr = ctr +1 
'''
