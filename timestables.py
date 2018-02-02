grid = [[format((x+1)*(y+1), '03') for y in range(0,12)]for x in range(0,12)]
print('My timestables')

for index in range(0,12):
        print(grid[index])

print('End')