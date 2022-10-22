from inspect import stack


def push(lst):
    bn = int(input("BN = "))
    bname = input("name = ")
    record = (bn, bname)
    lst.append(record)
    print(lst)
def pop(lst):
    del_rec = lst.pop()
    print(del_rec)

bstack = []
menu = '''OPTIONS:
1) push
2) pop
3) exit'''
while True:
    print(menu)
    op = int(input('Enter option number:  '))
    if op == 1:
        push(bstack)
    elif op== 2:
        pop(bstack)
    elif op == 3:
        print('thank u ')
        break
    else:
        print('invalid option')

