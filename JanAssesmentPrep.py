#Jan Assessment Preperation
#Cole Samson
#7/12/17
import random
team = []
for pX in range(0,4):
    team.append(str(input(("Team Name: "))))
team1 = random.choice(team)
team2 = random.choice(team)
while team1 == team2:
    if team1 == team2:
        team2 = random.choice(team)

print(team1)
answer1= random.randint(1,10)
print("please guess the random number")
guess1 = input()
counter1 = 0
while guess1 != answer1:
    print("please guess the number")
        if input() == answer1:

    counter1 = 1 + counter1
else:
    print("Correct")
print(t1, " had ", counter1, " attempts")

print(t2)
answer2= random.randint(1,10)
print("please guess the random number")
guess2 = input()
counter2 = 0
if guess2 != answer2:
    print("please guess the number")
    counter2 = 1 + counter2
else:
    print("Correct")
print(t2, " had ", counter2, " attempts")


