#file handling - read

#Declare name : array(5) of string
#Declare name : line of string
#Declare name : index of integer


name = []
fh = open('names.txt', 'r')
no_names = 0



line = fh.readline()
while line!= '':
    name.append[line]
    no_names += 1
    line = fh.readline()
fh.close()
message = ''
for index in range(0,no_names):
    message += str(name[index])
print(message)