#sum of numbers given by user until zero entered
num = float(input("Enter number       "))
total = 0
while num > 0:
    total = total + num
    num = float(input("Enter number or 0 to exit       "))
print ("Sum of the entered numbers is ", total)
print ("prog has ended")