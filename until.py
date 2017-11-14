def daysUntil(start, target):
    return target - start

def daysIn(month):
    if (month == 4) or (month == 6) or (month == 9) or (month == 11):
        nodays = 30
    elif (month == 2):
        nodays = 28
    else:
        nodays = 31
    return nodays