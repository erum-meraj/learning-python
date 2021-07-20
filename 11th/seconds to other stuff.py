#seconds to hrs n mins
sec = float(input("enter time in seconds "))
hr = int(sec/3600)
mins = int((sec%3600)/60)
rsec = sec%60
print(sec, "seconds = ", hr, "hours", mins, "min", rsec, "seconds")