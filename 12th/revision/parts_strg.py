#parts of a string

def get_text():
    file = open('string.txt', 'w')
    text  = input("Enter text: \n")
    file.write(text)
    file.close()

def read_text():
    file = open('string.txt', 'r')
    text = file.read()
    return text

def upper(text):
    up = 0
    for i in range(len(text)):
        if i.isupper() == True:
            up = up + 1
        else:
            continue
    print('Upper case letters  = ', up)
            
def lower(text):
    low = 0
    for i in range(len(text)):
        if i.islower() == True:
            low = low + 1
        else:
            continue
    print('lower case letters  = ', low)
    
def num(text):
    no = 0
    for i in range(len(text)):
        if i.isdigit() == True:
            no = no + 1
        else:
            continue
    print('Numbers  = ', no)

def sym(text):
    sb = 0
    for i in range(len(text)):
        if i.isalphanum() == False and i.isspace() == False:
            sb = sb + 1
        else:
            continue
    print('Symbols  = ', sb)


#main
get_text()
data = read_text()
print("OPTIONS \n  1) upper case letters \n 2) lower case letters \n 3) numbers \n 4) special characters")
op = int(input("Enter option:  "))
if op == 1:
    upper(data)
elif op ==2:
    lower(data)
elif op ==3:
    num(data)
elif op ==4:
    sym(data)
else:
    print("invalid op")
            
