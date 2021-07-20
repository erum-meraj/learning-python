#validity of triangle

#input
s1 = float(input("Enter 1st side"))
s2 = float(input("Enter 2nd side"))
s3 = float(input("Enter 3rd side"))

#conditions
if (s1 + s2)>s3 and (s2 + s3)>s1 and (s3 + s2)>s1:
      print ("the entered triangle is valid")
      
else:
      print("the entered triangle is invalid ")
      
