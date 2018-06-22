#Pre-release task
#16/03/18

import random
import time
i = 0
result = ''
nametime = []
#def alphaNumGen():
name = input("Enter name: ")
time1 = time.asctime()
print(name,time1)
nametime =  list((name + time1))
print(nametime)

while i < 6:
    j = random.choices(nametime)
    i = i + 1
    result = (str(result) + str(j))
print(result)
list(result)

#alphaNumGen()




