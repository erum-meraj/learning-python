
def push_ele(lst):
    n = int(input("Enter number of records to be entered:   "))
    for i in range(0,n):
        st_name = input("name:  ")
        marks = int(input("marks:  "))
        if marks >79:
            record = {st_name:marks}
            lst.append(record)
        else:
            continue
    return lst

def pop_ele(lst):
    if len(lst) <= 0:
        print('underflow')
    else:
        for i in range(0, len(lst)):
            popped_rec = lst.pop()
            print(popped_rec.keys())

mystack = []
menu = '''options:
1) push
2) pop
3) exit'''

while True:
    print(menu)
    op = int(input("op= "))
    if op ==1:
        push_ele(mystack)
    elif op == 2:
        pop_ele(mystack)
    elif op == 3:
        print("done")
        break
    else:
        print('invalid op')