std_dict = {}
roll = input("Enter student roll number (press n to exit)")
while roll != 'n' and roll != 'N':
    
    name = float(input("Enter name"))
    std_dict[roll] = name 
    roll = input("Enter student roll number (press n to exit)")

length = len(std_dict)
for ctr in std_dict:
    keys = std_dict.keys()
    while j>=0 and keys[j]:
        lst[j+1] = lst[j]
        j = j -1
    
    else:
        break
    lst[j+1]= t
else:
    print(lst)
print('prog ended')