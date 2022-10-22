
#finding prime numbers in a range of numbers 
n = int(input("Enter range limit:  "))
op = input('''Choose ur loop type:
    1. for --> type 1 
    2. while --> type 2
''')

if op == '1':
    for ctr in range(1, n+1):
        for div in range(2, ((ctr+1)//2)+1):
            if ctr % div == 0:
                break 
            else:
                continue
        else:
            print(ctr)
elif op == '2':
    ctr = 1
    while ctr <= n:
        div = 2
        while div <=(ctr+1)//2:
            if ctr % div == 0:
                break 
            div = div+1 
        else:
            print(ctr)
        ctr = ctr +1
else:
    print("invalid op")
