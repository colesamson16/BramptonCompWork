#enter a number - print all prime numbers less or equal to number
#report time taken for program
#find time for all primes less than 100,000

#importing libraries
import time
import math

iNum_of_primes = 0
iHighnum = 0

#determines whether number is prime
def primefun(num):
    if num < 2:
        return False

    i = 2
    for i in range(2, int(math.sqrt(num) + 1)):
        if (num % i == 0):
            return False

    return True



#Asks user for input
n = int(input("Enter a number: "))
#takes time
start_time = (time.clock())

B = range(2, n)

for i in B:
    if primefun(i):
        print(i)
        #sets i each time as highest prime number
        iHighnum = i
        #takes number of primes
        iNum_of_primes = iNum_of_primes + 1
#prints out info about primes
print('number of primes: ', iNum_of_primes)
print('Highest prime number', iHighnum)
endtime = time.clock()
#displays time taken
print("--- %s seconds ---" % (endtime - start_time))







