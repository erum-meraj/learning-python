lst = []
num = int(input("Enter number of elements: "))

for i in range(0,num):
    counter = 0
    n = int(input("Enter a number: "))
    temp = n

    while n>0:
        digit = n%10
        n = n//10
        counter = counter + 1

    if counter == 3:
        lst.append(temp)
    else:
        print("Enter 3 digit values only! Terminating the program...")
        break

length = len(lst)
print("Before sorting : ",lst)

for i in range(1,length):
    ctr = lst[i] % 10
    t = lst[i]
    j = i-1
    while j >= 0 and ctr < (lst[j] % 10):
        lst[j+1] = lst[j]
        j = j - 1
    lst[j+1] = t
print("List after sorting: ", lst)