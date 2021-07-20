# sum of values from a list with end with 3 
lst = eval(input("Enter list->"))
lst = list(lst)
length = len(lst)
tot = 0
for i in range(0, length):
    ele = lst[i]
    uni_ele = ele%10
    if uni_ele == 3:
        tot = tot + ele
    else:
        continue
    
print(lst)
print("sum ->  ", tot)