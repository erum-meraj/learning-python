#Write a programthat
# 1. prompts the user for a string
# 2. extracts all the digits from the string
# 3. if there are digits:sum the collected digits togetherprint out:original stringdigitssum of the digitsIf there are no digits:print the original string and a message "has no digits"
strg = input("Enter string->     ")
total = 0
length = len(strg)
print("the digits are: ")
for ctr in range(0, length):
    if strg[ctr].isdigit() == True:
        print(strg[ctr])
        total = total + int(strg[ctr])
    else:
        continue

print("sum of digits is ", total)  

