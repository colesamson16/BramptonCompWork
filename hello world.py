import datetime

print('What is your name')
name = input()
now = datetime.datetime.now().time()
if now >= datetime.time(12,0) and now <= datetime.time(17,30):
    now = 'Good Afternoon'
elif now >= datetime.time(5,0) and now < datetime.time(12,0):
    now = 'Good Morning'
else:
    now = 'Good Evening'
print('hello', name, 'and', now)