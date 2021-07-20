nums = eval(input("Enter numbers->      "))
total = 0
leng = len(nums)
for ctr in range (0 , leng):
    total = total + nums[ctr]
avg = total / leng
print ("the numbers entered-> ", nums)
print("Average->    ", avg)
