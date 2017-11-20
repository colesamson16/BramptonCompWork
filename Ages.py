#8 ages between 0 and 119 and tells me where the highest age is and where the lowest age is.
#Investigate how to generate random numbers.
#Extend program so that it generates 4000 ages and tells you where the highest and the lowest are.

import random

highval = -1
lowval = 5000
highpos = -1
lowpos = -1
ages = -1
for ages in range(1,9):
    num = int(random.randint(0,4000))
    if num > highval:
        highval = num
        highpos = ages

    if num < lowval:
        lowval = num
        lowpos = ages
#    for array in range(1,2):
 #       array = num
 #       print(num)
print("Lowest position is: ", lowpos)
print("Highest position is: ", highpos)
