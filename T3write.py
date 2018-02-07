#7/02/18
#Declare file as string
#declare inP as string

#opens file





inP = ''
file = open('tempfile.txt','w')


lines = []
while True:
    inP = input('Input String: ')
    file.write(str(inP))
    file.write('\n')
    if inP != '':
        lines.append(inP)
    else:
        break
text = lines

file.close()

