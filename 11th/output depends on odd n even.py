#output depends on odd n even 
import math
num = int(input("enter number"))
rem = num%2
if rem == 1 and num>0:
      ans = math.sqrt(num)
      print("root of ", num, "is",ans)
else:
      ans = (num)**3
      print("cube of ", num, "is",ans)