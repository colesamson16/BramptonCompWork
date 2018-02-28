#enter a number - print all prime numbers less or equal to number
#report time taken for program
#find time for all primes less than 100,000
#number of primes

import time
import math

num = int(input('Input a number'))
if num < 2:
    print('No prime numbers')
elif num == 2:
    print('2')
elif num > 2:
    print('2')
    for numcount in range(3,num):
        for div in range(2,numcount + 1):
            if (num / div) == 0:
                print('hello')
            elif num / div != 0:
                if numcount == div:
                    print(numcount)
                else:
                    print('sd')
else:
    print('Invalid input')







