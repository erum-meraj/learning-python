#nested ifelse driver insurance 
mar = int(input("Enter 1 -->married 0 --> unmarried      ")) 
if mar == 1:
    print("U r insured")
elif mar == 0:
    gend = int(input("Enter 1 -->female 0 --> male       "))
    if gend == 1:
        age = int(input("Enter age       "))
        if age> 25:
            print ("u r insured")
        else:
            print ("Sorry u r not insured")
    elif gend == 0:
        age = int(input("Enter age       "))
        if age> 30:
            print ("u r insured")
        else:
            print ("Sorry u r not insured")
    else:
        print("invalid input")
else:
    print("Invalid input")