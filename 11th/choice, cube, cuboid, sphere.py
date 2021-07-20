#choice, cube, cuboid, sphere
print('''choose shape
            1. cube
            2. cuboid
            3. sphere''')
opt = int(input("Enter choice"))
if opt == 1:
      side = float(input("enter side length"))
      sa = 4*side*side
      vol = side**3
      print ("Surface area = ", sa)
      print ("volume = ", vol)
elif opt == 2:
      leng = float(input("enter length"))
      br = float(input("enter breadth"))
      hei = float(input("enter height"))
      sa = 2*((leng*br)+(leng*hei)+(hei*br))
      vol = leng*br*hei
      print ("Surface area = ", sa)
      print ("volume = ", vol)
else:
      pi = 22/7
      r = float(input("enter radius"))
      sa = 4*pi*r*r
      vol = (3/4)*pi*r*r*r
      print ("Surface area = ", sa)
      print ("volume = ", vol)

