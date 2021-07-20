#alphanumeric string given, sum of the digits in the number
#display -> numbers, string, sum
string = input("ENter the string:  ")
ttl = 0
print("Given string =>  ", string)
print("DIgits in the string => ")
for ctr in range(0,len(string)):
    if string[ctr].isdigit() == True:
        ttl = ttl + int(string[ctr])
        print (string[ctr])
if ttl == 0:
    print("none")
    print("the num has no digits ") 
else:   
    print("Sum of the digits =>  ", ttl)


