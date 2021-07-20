# mul table
#%%%
#while loop
num = int(input("Enter number : "))
mul = int(input("Enter number of multiples: "))
ctr = 1
while ctr <= mul:
    print(num, "x" , ctr, " = ", num*ctr)
    ctr = ctr +1
#%%
num = int(input("Enter number : "))
mul = int(input("Enter number of multiples: "))
for ctr in range(1, mul +1 ):
    print(num, "x" , ctr, " = ", num*ctr)