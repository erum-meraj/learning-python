

stack = []
top = -1

# push function
def push(ele):
    global top
    top += 1
    stack[top] = ele

# pop function
def pop():
    global top
    ele = stack[top]
    top -= 1
    return ele
# Function that returns 1 if string is a palindrome
def isPalindrome(string):
    global stack
    length = len(string)
    stack = ['0'] * (length + 1)
    mid = length // 2
    i = 0
    while i < mid:
        push(string[i])
        i += 1

    # Checking if the length of the string is odd then neglect the middle character
    if length % 2 != 0:
        i += 1

    # While not the end of the string
    while i < length:
        ele = pop()
        if ele != string[i]:
            return False
        i += 1
    return True


print (' 1 - Input a string')
print ('2- Check if the string is palindrome or not')
print('3 - exit')
choice=int(input("Enter your choice: "))
while True:
    if choice == 1:
        string= input('Enter the desired string')
    elif choice == 2:
        if isPalindrome(string):
            print("Yes, the else: string is a palindrome")
        else:
            print("No, the string is not a palindrome")

    elif choice == 3:
        break
    else:
        print('Invalid option')
        break
    print (' 1 - Input a string')
    print ('2- Check if the string is palindrome or not')
    print('3 - exit')
    choice=int(input("Enter your choice: "))


















