from num2words import num2words
t_car = ("toyota", "Honda", "GM", "Ford", "BMW", "Volkswagon", "mercedes", "Ferrari", "Porsche")
count = 1
for ctr in range(2, 7):
    
    print(num2words(count), "        ", t_car[ctr])
    count += 1