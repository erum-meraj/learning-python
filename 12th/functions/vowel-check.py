def check(stg):
    if len(stg) == 1:
        if stg.capitalize() in ['A', 'I' ,'O', 'U', 'E' ]:
            print("Vowel")
        else:
            print("Consonant")

#_main_
letter = input("Enter letter :   ")
if letter.isalpha() == True:
    check(letter)
else:
    print("Not a letter")