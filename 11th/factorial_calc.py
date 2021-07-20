num = int(input("digit = "))
prod = 1
for num in range(1,num+1):
        prod = prod * num
        num = num - 1
print(prod)