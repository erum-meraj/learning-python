num = int(input("ENter number of terms"))
t1 = 1
t2 = 0
output = list()
if num > 0:
    for ctr in range(0, num):
        t2 = t2 + t1
        t1 = t2 - t1
        output.append(t2)
else:
    print("Given number must be more than Zero")
print(output)