list = []
list2 = [1,2,4,8]
list3 = []
for y in range(0,4):
    print("enter binary digit")
    for x in range(0,4):
        for z in range(0,4):
            list[x] = input()
            for b in range(0,4):
                list3 = list[x] * list2[z]
sum = list[0] + list[1] + list[2] + list[3]
print(sum)

