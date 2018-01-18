# Pizza ordering system
# Ian Simpson
# 3rd January 2018

# DECLARE order : STRING
# DECLARE orderNo : INTEGER
# DECLARE base : CHAR
# DECLARE choice : INTEGER
# DECLARE again : CHAR
# DECLARE topName : ARRAY[0..9] OF STRING
# DECLARE topAmnt : ARRAY[0..9] OF INTEGER
# DECLARE topCount : INTEGER
# DECLARE index : INTEGER
# DECLARE shopOpen : BOOLEAN
# DECLARE endOrder : BOOLEAN

topName = ['Cheese', 'Ham', 'Pepperoni', 'Pineapple', 'Mushroom', 'Cherry tomatoes', 'Chicken', 'Peppers', 'Olives',
           'Jalapenos']
topAmnt = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
orderNo = 1
shopOpen = True


def displayStock():
    print('Toppings available:')
    for index in range(0, 10):
        print(str(index) + ' ' + topName[index] + ' ' + str(topAmnt[index]))


displayStock()

order = 'Order no ' + str(orderNo) + ': '
base = input('Enter your choice of base (T)hin or (P)an: ')
while base.upper() != 'T' and base.upper() != 'P':
    print('Not a valid base type. Try again.')
    base = input('Enter your choice of base (T)hin or (P)an: ')

if base.upper() == 'T':
    order = order + 'Thin base. '
else:
    order = order + 'Pan base. '


endOrder = False
topCount = 0
while base.upper() != 'Y' and base.upper() != 'N':
    choice = int(input('Enter topping number (0-9): '))
    while choice < 0 or choice > 9:
        print('Not a valid topping choice. Try again.')
        choice = int(input('Enter topping number (0-9): '))
    order = order + topName[choice] + '. '
    print(order)
again = input('Do you want another topping[y/n]')

