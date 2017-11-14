from until import *
currDay = int(input("Enter current day number"))
currMonth = int(input("Enter current month number"))
futDay = int(input("Enter future day number"))
futMonth = int(input("Enter future month number"))
totalDays = 0
for thismonth in range(currMonth,futMonth+1):
    if thismonth < futMonth:
        totalDays = totalDays + daysIn(thismonth)
    else:
        totalDays = totalDays + daysUntil(currDay,futDay)
print(totalDays)
