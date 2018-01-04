#The Pizza Co.
#Cole Samson
#4/01/18

#Declare order: string
#Declare orderno: integer
#Declare base: string
#Declare choice: string
#Declare again: string
#Declare topcount: integer
#Declare index: integer
#Declare shopopen: boolean
#Declare endorder: boolean
#Declare i: integer
#Declare foo: integer
#Declare var: string
#Declare thin: string
#Declare pan: string
choices = []
orderno = []
def deftop():
    choice = input('Please select a topping[0...9')
    while choice > 9 or choice < 0:
        print('invalid input please try again')
        choice = input('Please select a topping[0...9')
        break
    choices.append = choice
order = ''
base = ''
i=0
foo = 12

topname = ['cheese', 'ham', 'pepperoni', 'pineapple',
           'mushroom', 'cherry tomatoes', 'chicken', 'peppers', 'olives', 'jalapenos']
topamnt = [10,10,10,10,10,10,10,10,10,10]
for i in range(0,10):
    print(i, topname[i], topamnt[i])
order = input('Do you want [T]hin or [P]an base?')
while order != 'T' or 't' or 'P' or 'p':
    print('invalid input please try again')
    order = input('Do you want [T]hin or [P]an base?')
    break
for c in range(0,5):
    deftop()
    again = input('Do you want another topping [y/n]')
    if again == 'y' or 'Y':
        deftop()
    elif again == 'n' or 'N':
        print(choices, '', base)





if order == 'T' or 't':
    base = 'Thin'
elif order == 'P' or 'p':
    base = 'Pan'








