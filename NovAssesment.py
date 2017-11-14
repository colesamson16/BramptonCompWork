#Cole Samson 9/11/17 As/Comp/a

counter = 0
teamname = "Zeus"
playerHits = 0
totalHits = 0
averageHits = 0.0
pointsEarned =


def getdetails():
    global teamname, playerHits, totalHits, counter
    teamname = input("Team Name: ")
    for counter in range(0,6,):
    playerHits = int(input("Enter Player Hits: "))
    totalHits = totalHits + playerHits
def calcval():
    global pointsEarned, totalHits
    averageHits = totalHits/6
    if totalHits > 50:
        pointsEarned = 1
    elif averageHits >= 10:
        pointsEarned = pointsEarned + 1
def outputres():
    global teamname, pointsEarned
    print(teamname," has scored ", pointsEarned)

getdetails()
calcval()
outputres()
