#input term analysis
term = input('Enter sentence\n')
#alpha
vow = 0
cons = 0
for ctr in term:
    if ctr.isalpha() == True:
        if ctr=='A' or ctr=='a' or ctr=='E' or ctr =='e' or ctr=='I' or ctr=='i' or ctr=='O' or ctr=='o' or ctr=='U' or ctr=='u':
            vow = vow + 1
        else:
            cons =cons + 1
print("vowels = ", vow)
print("consonants = ", cons)
#numbers           
num = 0
for ctr in term:
    if ctr.isnumeric() == True:
        num = num +1
print("numbers = ", num)
#special chars
sym = 0
for ctr in term:
    if ctr.isnumeric() == False and ctr.isalpha() == False:
        sym = sym +1
print("Special chars = ", sym)
