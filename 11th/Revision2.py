#sum of odd n evenn
num = int(input("Enter number of natural numbers:    "))
sum_even = 0
sum_odd = 0
for num1 in range(1 , num +1):
      if (num1 % 2) == 0:
            sum_even += num1
      else:
            sum_odd += num1

print ("Sum of even numbers =   ", sum_even)
print ("Sum of odd numbers =   ", sum_odd)           
