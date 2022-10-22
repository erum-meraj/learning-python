'''
Program to calculate simple interest using a function interest() that can receive principal amount, time and rate, and returns calculated simple interest. Do specify default values for rate and time as 10% and 2 years respectively.
'''
def interest(p_amount, rate = 10, time = 2):
    Simple_interest=(p_amount*time*rate)/100
    print('The simple interest is:',Simple_interest)

#main
principle=float(input('Enter the principal amount:'))
time=int(input('Enter the time(years) :'))
rate=float(input('Enter the rate:'))
interest(principle, rate, time)



