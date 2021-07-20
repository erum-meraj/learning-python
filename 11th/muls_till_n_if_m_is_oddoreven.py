#n no. of numbers n print if divisible by m n if its odd or even
n = int(input("Enter no. of numbers        "))
m = int(input("Enter divisor      "))
for a in range(1, n + 1):
    rem = a%m
    if rem == 0:
        
        EorO = a%2
        if EorO == 0:
            print (a, "->  even")
        else:
            print(a,"->  odd")
    else:
        continue