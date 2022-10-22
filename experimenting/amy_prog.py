#Delhi Vidyut Board that will generate the Electricity Bill based on
#the current and old meter readings of an electricity meter.
units = int(input("Enter number of units used:   "))
total_cost = 250
if units >= 100:
    extra = units - 100
    total_cost = 100*3.25
    total_cost = total_cost + extra*4.75
else:
    total_cost = units*3.25
service = total_cost*11.5/100
total_cost = total_cost + service
print("Total cost = ", total_cost) 
