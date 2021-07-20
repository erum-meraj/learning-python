#bubble sorting of 3 digit number list
# [764, 873, 982, 991]
lst = eval(input("Enter a three digit numbers list = "))
length = len(lst)
for i in range(1,length):
    ele = str(lst[i])
    if len(ele) == 3:
        temp = lst[i]%10
        t = lst[i]
        j = i-1
        while j>=0 and temp<(lst[j]%10):
            lst[j+1] = lst[j]
            j = j -1
    
    else:
        break
    lst[j+1]= t
else:
    print(lst)
print('prog ended')