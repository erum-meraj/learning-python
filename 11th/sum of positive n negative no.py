num = int(input("Enter the number ->    "))
sum_pos = 0
sum_neg = 0
while num != 0:
    if num > 0:
        sum_pos = sum_pos + num
    else:
        sum_neg = sum_neg + num
    num = int(input("Enter the number (0 to exit) ->    "))

print  ("Prog has ended")
print ("Sum of +ve numbers = ", sum_pos)
print ("Sum of -ve numbers = ", sum_neg)