#cole samson 22/01/17 3x3 2d array

#Declare numarray:Array[1..9],[1..9] as integer
#Declare counter as integer
#Declare numleft:Array[] as integer

import random
counter = 0
numarray = [[0 for col in range(0,3)] for row in range(0,3)]
numleft = [1,2,3,4,5,6,7,8,9]
int = 0
ans = ''

print('''

|--------------------|
|        Menu        |
| a. random grid     |
| b. user input grid | 
|--------------------|
''')
print('''

Enter function a or b
''')

ans = str.lower(input())
if ans == 'a':
    for col in range(0,3):
        for row in range(0,3):
            added = False
            while added != True:
                counter = random.randint(1,9)
                if counter in numleft:
                    numarray[row][col] = counter
                    numleft.remove(counter)
                    added = True

    for index in range(0,3):
        print(numarray[index])

elif ans == 'b':
    for col in range(0, 3):
        for row in range(0, 3):
            numarray[row][col] = input('Enter number')
    for index in range(0, 3):
        print(numarray[index])


