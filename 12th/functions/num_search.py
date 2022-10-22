def linear_sch(lst, n):
    for i in range(0, len(lst)):
        if lst[i] == n:
            print("Element found at index: ", i)
            break
    else:
        print("Element no found")   
def binsearch(ar,key,low,high):
    #idk this part
    print(":)")           
def sort(lst):
    n = len(lst)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if lst[j] > lst[j + 1] :
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    print(lst)
    print("Smallest element: ", lst[0])

#main
lst = eval(input("Enter list:  "))
ele = int(input("Enter element to search:  "))
op = int(input('''Enter 1 for linear search
2 for binary search:\n'''))
if op == 1:
    linear_sch(lst, ele)
elif op == 2:
    binsearch(lst, ele)
else:
    print(":)")
sort(lst)
