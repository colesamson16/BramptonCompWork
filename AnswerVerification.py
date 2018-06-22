#DECLARE Question: STRING
#DECLARE AnsVerify: BOOLEAN
#DECLARE User_Ans: STRING
#DECLARE Answer: STRING #insert answer from file (FINN)
#DECLARE loopy: INTEGER # it till loop 20 times

Question = "Is a compiler a type of translator?"#This will be question from file should generate a new question each time #finn
Answer = "A compiler is a type of translator " #This will be answer from file with the following question #finn

Ans_Verify = False
Count = 0
loopy = 20

for loopy in range(0,loopy):
    print(Question)
    print(Answer)
    User_ans = str(input("Please enter 'y' if you achieved the correct answer and please enter 'n' if you achieved the incorrect answer:"))
    while User_ans != "n" and User_ans != "y":
        print("Please type in either 'y' or 'n'")
        User_ans = str(input("Please enter 'y' if you achieved the correct answer and please enter 'n' if you achieved the incorrect answer:"))

    if User_ans == "y":
        Ans_Verify = True
        Count = Count + 1
        print("Well done you have 1 more point")
        print("Here is your current count: ",Count)
    elif User_ans == "n":
        Ans_Verify = False
        print("Don't worry just try again.")
print("Here is your final count: ", Count)