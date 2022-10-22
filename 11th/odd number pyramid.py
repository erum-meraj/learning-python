#odd number pyramid
num = int(input("ENter number of rows"))
for rows in range(1, num+1):
    for col in range(1, rows +1):
        print( (2*col) - 1, end= " ")
    print("  ") 