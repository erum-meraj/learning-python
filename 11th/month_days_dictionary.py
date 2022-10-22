#dictionary of maths and ops on its
main_set = {"January " :31, "February" :28, "March":31 , "April":30 , "May" :31 , "June":30 , "July":31, "August" :31 , "September":30 , "October" :31 , "November" :30, "December":31}

#part A
try:
    month = input("Enter month->   ")
    print(month, " has ", main_set[month], " days" )
except:
    print("Such a month does not exist")
print("-"*15)

#part B
print(sorted(main_set))
print("-"*15)

#part C
print("months with 31 days:")
for ctr in main_set:
    if main_set[ctr] == 31:
        print(ctr)
    else:
        continue
print("-"*15)

#part D
v = sorted([(ctr1,ctr2) for ctr2, ctr1 in main_set.items()])
print(v)
print("-"*15)
