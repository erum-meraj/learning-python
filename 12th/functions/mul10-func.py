#10 multiples for given number using functions
def mul(num):
    for i in range(1, 11):
        print(num, " x ", i , ' = ', num*i)
n = int(input("Enter number:    "))
mul(n)