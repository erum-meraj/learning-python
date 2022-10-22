#star pyrd
n= 4
for rows in reversed(range(1, n+1)):
    for col in range(1, rows +1):
        print("*", end = "")
    print(" ")
