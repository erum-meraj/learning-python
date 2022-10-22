def comp(num):
    if num == 1:
        return 1 
    else:
        return (num + comp(num-1))

lim = int(input("Enter number:   "))
total = comp(lim)
print(total)
