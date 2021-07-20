#roots of quadratic eqn
import math
#coefficiants
print ("general form of quadratic eqn is ax^2 + bx + c")

c1 = int(input("a = "))
c2 = int(input("b = "))
c3 = int(input("c = "))

#calc
d = (c2*c2) - 4*c1*c3

if d>0:
      root1 = (-(c2) + math.sqrt(d))/(2*c1)
      root2 = (-c2 - math.sqrt(d))/(2*c1)
      print("the roots r ",root1,"," , root2)

elif d == 0:
       root1 = (-(c2) + math.sqrt(d))/(2*c1)
       print("this equation has only one root which is ",root1 )


else:
      root1 = complex((-(c2) + math.sqrt(d))/(2*c1))
      root2 = complex((-(c2) - math.sqrt(d))/(2*c1))

      print("this equation has complex roots")
      print("the roots r ",root1,"," , root2)
