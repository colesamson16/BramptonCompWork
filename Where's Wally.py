#where's wally
#cole samson
#25/01/18

import random
col = 0
row = 0
whereswally = [['M' for col in range(0,5)] for row in range(0,5)]



wallyx = int(random.randint(0,4))
print(wallyx)
wallyy = int(random.randint(0,4))
print(wallyy)
whereswally[wallyy][wallyx] = 'W'
for index in range(0,5):
        print(whereswally[index])

endGame = False
while endGame != True:
    guessx = int(input('Please enter x coordinate of Wally: '))
    while guessx > 5 or guessx < 1:
        print('invalid input try again')
        guessx = int(input('Please enter x coordinate of Wally: '))

    guessy = int(input('Please enter y coordinate of Wally: '))
    while guessy > 5 or guessy < 1:
        print('invalid input try again')
        guessy = int(input('Please enter y coordinate of Wally: '))

    if (guessx - 1) != wallyx or (guessy - 1) != wallyy:
        print('Wrong')
    else:
        print("You've Won")
        endGame = True