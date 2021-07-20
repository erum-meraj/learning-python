#input 2 numbers n check if odd n +ve -> sqr otherwise cube
def calc(n1, n2):
    #number 2 
    if n1> 0:
        if n1 % 2 == 1:
            ans1 = n1**2
            
        else:
            ans1 = n1**3
    else:
        ans1 = n1**3
    #number 2 
    if n2> 0:
        if n2 % 2 == 1:
            ans2 = n2**2
            
        else:
            ans2 = n2**3
    else:
        ans2 = n2**3
    return ans1, ans2


#_main_
n1  = int(input("1st num:   "))
n2  = int(input("2nd num:   "))
a1 , a2 = calc(n1, n2)
print('Answer 1: ', a1, '\nAnswer 2:', a2)