
def calc(n):
    if n in range(1000, 10000):
        a = n//100
        b = n%100  
        print(a**2 + b**2)
    else:
        print("Not a 4 digit number")
        
num = int(input("number:  "))
calc(num)
        
    