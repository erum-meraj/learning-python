def inc(lst):
    for ctr in range(1, len(lst)):
        if ctr%2 == 1:
            lst[ctr] =lst[ctr] + 2
        else:
            continue
    print("Modified list:   ", lst)

#_main_
mylst = eval(input("Enter list:   "))
inc(mylst)   
print(mylst)