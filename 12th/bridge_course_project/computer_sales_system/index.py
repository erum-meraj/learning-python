#The  software  computer  sales  and  service  system  allow  the  user  to get  good quality computer parts and computer services.
print(''' \n\n                 COMPUTER SALES AND SERVICE SYSTEM\n\n
1. to buy computer parts.
2. to ask for computer service.
3. register your problems in the software or service
4. to see various comments and ratings on our software 
5. exit 
\n
''')
op = int(input("Enter your choice:    "))
print('\n\n\n')
if op == 1:
    import buying_parts
elif op == 2:
    import service
elif op==3:
    import problem_reg
elif op==4:
    import comment_view
else:
    print("Thank you :) ")
