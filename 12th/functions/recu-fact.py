def fact(n):
    if n == 1:
        return 1
    else:
        return(n*fact(n-1))

num = int(input("Enter number:    "))
fac = fact(num)
print(num,"!  =  ", fac)