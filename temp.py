#C to F
scotC = 12
italC = 23
def CtoF():
    print("Please enter degrees C")
    C = input()
    F = C * (9 / 5) + 32
    print(F)


def FtoC():
    print("Please enter degrees F")
    F2 = input()
    C2 = (int(F2) - 32) * (5 / 9)
    print(int(C2))
    print(scotC)
    print(italC)
print("""
|=============|
|    Menu     |
| 1. C to F   |
| 2. F to C   |
|=============|
""")
x = int(input())
if x == 1:
    CtoF()
elif x == 2:
    FtoC()
else:
    quit()
