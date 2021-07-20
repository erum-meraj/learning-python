#checking if prime using functions
def prime(num):
    for ctr in range(2, num//2):
        if num%ctr == 0:
            print("Not prime")
            break
        else:
            continue
    else:
        print("Prime")

#_main_
n = int(input("Enter number:  "))
prime(n)