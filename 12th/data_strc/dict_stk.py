
def PUSH(stk,k):
    stk.append(k) 
def POP(S):
    if S!=[]:
        return S.pop()   
    else:
        return None 
#main
menu = '''OPTIONS:
1. Enter key: value pair into student dictionary 
2. Display student dictionary 
3. Students with marks greater than input value\n'''
run = 1 
main_dict = {}
while run ==1:
    print(menu)
    op = int(input("Enter option number:   "))
    if op == 1:
        num = int(input("Enter number of students :  "))
        for i in range(num):
            stu = input("Enter student name:  ")
            marks = int(input("Enter marks:  "))
            main_dict[stu] = marks
    elif op == 2:
        for i in main_dict:
            print('Student: ',i , '   Marks: ', main_dict[i])
    elif op == 3:
        stk=[] 
        lim = int(input("Enter min marks:   "))
        for k in main_dict:
            if main_dict[k]>=lim:
                PUSH(stk,k) 
        print("Students with marks more than ", lim)
        while True:
            if stk!=[]:
                print(POP(stk))  
            else:
                break 
    else:
        print("Invalid option.")
    run = int(input('''\nEnter 
1) Another operation 
2) exit \n'''))