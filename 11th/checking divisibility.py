#checking divisibility
divisor = float(input("Enter the divisor"))
divident = float(input("Enter divident"))
rem = divident%divisor
if rem == 0:
    pass
    print(divident, "is divisible by ", divisor)

else:
    print(divident, "is not divisible by", divisor)
