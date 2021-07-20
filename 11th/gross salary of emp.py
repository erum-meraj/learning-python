#employee salary

sal = float (input("enter employee salary"))


if sal<1500:
       hra = (sal * 10)/100
       da = (sal * 90)/100

       print ("Gross salary = ", sal+hra+da)
else:
      hra = 500
      da = (sal * 98)/100
      print ("Gross salary = ", sal+hra+da)

