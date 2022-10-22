def total(lst):
    tot = 0 
    for i in lst:
        tot = tot + i 
    print(tot)
    return
lst = eval(input("list: "))
total(lst)