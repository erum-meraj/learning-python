#perform ops on list. ops -> searching, inserting, removing 
def lst_rem(lst, ind):
    if ind not in range(len(lst)):
        print("Index out of range")
    else:
        ele = lst.pop(ind)
        print("Element removed ->  ", ele)
        print("final list -> ", lst)
    return
def lst_inst(lst, ele, index):
    lst.insert(index, ele)
    print("Final list ->  ", lst)
    return
def lst_srch(lst, ele):
    for i in range(len(lst)):
        if lst[i] == ele:
            print('Element found at index:  ', i)
            break 
        else:
            continue
    else:
        print("Element not found")
    return

#main
menu = '''
    OPERATIONS:
1. Insert element
2. remove element 
3. search element 
4. exit \n\n'''

lst = eval(input("Enter list:    "))
run = 1
while run == 1 :
    print(menu)
    op = int(input("Enter operation number:    "))
    if op == 1:
        ele = input("\nEnter element to be inserted:   ")
        ind = int(input("Enter index:  "))
        lst_inst(lst, ele, ind)
    elif op == 2:
        ind = int(input("\nEnter index number:   "))
        lst_rem(lst, ind)
    elif op == 3:
        ele = input("Enter element to search:   ")
        lst_srch(lst, ele)
    run = int(input('''\n\n0. exit
1. another operation
enter option:   '''))

print("\nthank u ")