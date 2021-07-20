#cont n cur dictionary

final_dict = {}
cont = input("Enter country(press n to exit) ->   ")
while cont != 'n' and cont != 'N':
    
    cur = input("Enter currency ->    ")
    final_dict[cont] = cur
    cont = input("Enter country(press n to exit) ->   ")

#tabular display
print("Country", 23*" ", "Currency")
for ctr in final_dict:
    leng = len(ctr)
    spaces = 30 -leng
    
    print(ctr, spaces*" ", final_dict[ctr])

#searching 
seacrh_cont = input("Enter country name  ->   ")
search_cur = final_dict[seacrh_cont]
print("currency ->    ", search_cur)