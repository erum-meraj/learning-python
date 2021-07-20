#+5 to odd values and +10 to even values of a list 
L = eval(input("Enter list->"))
L = list(L)
length = len(L)
for i in range(0, length):
    if L[i]%2 == 0:
        L[i] = L[i] + 10
    else:
        L[i] = L[i] + 5
print(L)