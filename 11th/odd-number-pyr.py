#odd number pyramid
num1 = int(input("ENter number of rows"))
for rows in range(1, num1+1):
    for col in range(0, rows):
        print((2*(col)+ 1), end = "  ")
    print("  ")