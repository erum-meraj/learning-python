#changing the case of the string repeatedly
string = input("Enter string:     ")
while string != 'q' and string != 'Q':
        for ctr in range(0, len(string)):
            if string[ctr].isalpha() == True:
                if string[ctr].isupper() == True:
                    final_let = string[ctr].lower()
                    print(final_let, end = "")
                else:
                    final_let = string[ctr].upper()
                    print(final_let, end = "")
            else:
                print(string[ctr], end = "")
        print(" ")
        string = input("Enter string (enter q to exit):     ")

print("Prog ended")