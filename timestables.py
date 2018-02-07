#Declare grid: integer
#Declare index: integer

#print out timestable

grid = [[format((x)*(y), '3') for y in range(1,13)]for x in range(1,13)]

print('My timestables')

for index in range(0,12):
        print(grid[index])

print('End')