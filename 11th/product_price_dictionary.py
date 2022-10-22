#product and price dictionary

final_prods = {}
k = input("Enter product(press n to exit)")
while k != 'n' and k != 'N':
    
    pri = float(input("Enter price"))
    final_prods[k] = pri
    k = input("Enter product(press n to exit)")
print("the products are :  ", final_prods)
print(final_prods.keys())