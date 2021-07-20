h = int(input("Enter Z height :   "))
#first row
for row in range(0, h):
    print("*", end = " ")
print(" ")
for spaces in reversed(range(1,h+1)):
    print(" "*(spaces*2 -1), "*")
for row in range(0, h):
    print("*", end = " ")
print(" ")
    
