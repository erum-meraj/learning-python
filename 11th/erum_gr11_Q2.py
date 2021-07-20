
lst = eval(input("Enter list ->    "))

for i in range(1, len(lst)):
    ref_val = lst[i] % 10
    ele = lst[i]
    j = i-1
    if lst[i] > 99 and lst[i]  < 1000:
        while j >= 0 and ref_val < (lst[j] % 10):
            lst[j+1] = lst[j]
            j = j - 1
        lst[j+1] = ele
    
    else:
             print("Program has ended. Only 3 digit numbers allowed. ")
             print("LIST NOT SORTED ")
             break
    if i == (len(lst)-1) :
            print("List is sorted ")
print ("FINAL LIST:", lst) 
