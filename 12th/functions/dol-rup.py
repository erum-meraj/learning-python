def conversion(amt, rate):
    print("$",amt, " = ", "₹",amt*rate)

#_main_
amt = float(input("Enter amount (in dollars):  "))
rate = float(input("Enter rate:  "))
conversion(amt, rate)

    