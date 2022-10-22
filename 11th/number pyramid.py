#upside down dec number pyramid
num = int(input("ENter number of rows u want in the pyramid "))
for rows in reversed(range(1, num + 1)):
    for col in range (0, rows):
        print (num - col, end = "  ")
    print(" ")
            