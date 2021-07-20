#CHECKING IF THE GIVEN NUMBER IS PRIME OR NOT 
num = int(input("enter number   "))
divisor = 2

if num == 1:
    print("You have entered 1")
else:
    #CHECKING IF COMPOSITE
    for divisor in range(2, num//2):
        rem = num%divisor 
        if rem == 0:
            print(num, " is composite")
            break
    #PRINTING PRIME 
    else:
        print (num, "is prime")