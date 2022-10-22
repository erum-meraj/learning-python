# Input a list of ‘L’elementsfrom the user. 
# Multiply an element by 2 if its odd index. Display the final list.  
# Alsofind and display the sum of all the values which are ending with 3f
lst = eval(input("Enter the list:   "))
length = len(lst)
total = 0
for ctr in range(0, length):
    ele = lst[ctr] 
    
    if ele%10 == 3:
        total = lst[ctr] + total
    else:
        continue 

for ctr in range(0, length):
    ele = lst[ctr] 
    if ctr %2 ==1 :
        ele = lst[ctr]*2
        lst[ctr] = ele
    else:
        continue
print("Final list ->   ", lst)
print ("sum of all the values which are ending with 3 ->   ", total)

