final_dict = {}

name = input("Enter team name (press n to exit) =>        ")
while name != 'n' and name != 'N':
    
    results = eval(input("Enter results [Wins, losses] =>      "))
    final_dict[name] = results
    name = input("Enter team name (press n to exit) =>        ")
print(" ")
print("the final results are :  ", final_dict)
print(" ")
print("-"*15)
print(" ")

#part A
team = input("Enter team name")
lst = final_dict[team]
win_per = (lst[0]/(lst[1] + lst[0]))*100
print("win % = ", win_per)
print(" ")
print("-"*15)
print(" ")

#part B
wins_of_teams = list()
for ctr in final_dict:
    result1 = final_dict[ctr]
    wins = result1[0]
    wins_of_teams.append(wins)
print("No. of wins by teams =>    ",wins_of_teams)
print(" ")
print("-"*15)
print(" ")

#part C
count = 0
for ctr in final_dict:
    print(ctr, " - ", wins_of_teams[count] )
    count += 1
