
def create_lst():
    length = int(input('Enter number of elements in list:   '))
    lst = []
    for i in range(length):
        ele = input('Enter element:   ' )
        lst = lst + [ele]
    return lst

def search(lst):
    ele = input('Element to be searched :  ')
    for i in range(0,len(lst)):
        if lst[i] == ele:
            print('Element found at index ', i)
            break
    else:
        print('Element not found')


menu = '''OPTIONS:
1) enter list
2) search in list
3) exit'''

while True:
    print(menu)
    op = int(input('Enter option number:  '))
    if op == 1:
        lst = create_lst()
        print(lst)
    elif op== 2:
        search(lst)
    elif op == 3:
        print('thank u ')
        break
    else:
        print('invalid option')
