#2D Array 18/1/18
#declare timmeh:Array[1...2,1...6] of char


timmeh = [['Messi', '22', '2'], ['Ronaldo', '32','5'], ['Benzema', '21','3'], ['Bale', '14', '4'], ['Kroos', '7', '-1'], ['Suarez', '30','0']]
print(timmeh)

index = 1
while index != -1:
    print(timmeh[index][0])
    index = int(timmeh[index][2])