
#Function to print squares n cubes of keys in a dictionary

#function 
def sqr(): 
    n=int(input("Enter the number of keys:   "))
    dict={} 
    for i in range(1,n+1):
        dict[i]=i**2 
    print("dict = ", dict)
    
def cube(): 
    n=int(input("Enter the number of keys:   "))
    dict={} 
    for i in range(1,n+1):
        dict[i]=i**3 
    print("dict = ", dict)

#main
op = int(input('''1) key: square
2) key: cube
ENter option:  '''))
while op != 0: 
    if op == 1:
        sqr()
    elif op == 2:
        cube()
    elif op == 0:
        print("Thank u ")
        break  
    else:
        print("invalid option")
        break
    op = int(input('''1) key: square
2) key: cube
enter 0 to exit the prog
ENter option:  '''))
    

        



