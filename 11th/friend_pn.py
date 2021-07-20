#friend n phone no. dict
final_dict = {}
nf = int(input("no. of friends->   "))
if nf >= 5:
    name = input("Enter friend's name (press n to exit) =>        ")
    while name != 'n' and name != 'N':
        pn = int(input("Enter phone number =>      "))
        final_dict[name] = pn
        name = input("Enter friend's name (press n to exit) =>       ")
    print(" ")
    print("the final dict are :  ", final_dict)

fri = input("Enter friend's name->   ")
req_n = final_dict[fri]

print("phone number", req_n)