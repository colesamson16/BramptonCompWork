#7/02/18
#Declare file as string
#declare inP as string

#opens file
file = open('tempfile.txt','w')
#asks user for input
inP = input('Input String: ')
#writes user input
file.write(inP)
file.close()
#opens and displays user input
file = open('tempfile.txt', 'r')
print(file.read())