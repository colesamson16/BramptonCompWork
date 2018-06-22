#Cole Samson Flashygame Interface
NumOfLine = 0
def Filereader (NumofLine):
    NumOfLine = 0
    i = 0

    file = open("QuestionAnswerFileData.txt")

    # opening file

    for line in file.readlines():
        NumOfLine = NumOfLine + 1

    # counting number of lines in text document

    Section = []
    Question = []
    Answer = []

    file = open("QuestionAnswerFileData.txt")

    for line in file.readlines(NumOfLine):
        # going through each line in txt file
        line = line.strip()
        # stripping each line of un-needed whitespace
        Section.append(0)
        Question.append(0)
        Answer.append(0)
        # adding a new value to each array

        str.replace("\t", "", "")
        # replacing the \t with spaces (temp method)
        Linearray = line.split('&')
        # the line is split into three sections seperated by the & sign

        Section[i] = Linearray[0]
        Question[i] = Linearray[1]
        Answer[i] = Linearray[2]
        i = i + 1

    # each array is assigned its value of the fragmented string

    print(Section)
    print(Question)
    print(Answer)

    return NumOfLine

    # Array values are printed out
print(NumOfLine)
def AnsVerify():
    # DECLARE Question: STRING
    # DECLARE AnsVerify: BOOLEAN
    # DECLARE User_Ans: STRING
    # DECLARE Answer: STRING #insert answer from file (FINN)
    # DECLARE loopy: INTEGER # it till loop 20 times

    Question = for Question[i] in range(0,NumOfLine)  # This will be question from file should generate a new question each time #finn
    Answer = "A compiler is a type of translator "  # This will be answer from file with the following question #finn

    Ans_Verify = False
    Count = 0
    loopy = 20

    for loopy in range(0, loopy):
        print(Question)
        print(Answer)
        User_ans = str(input(
            "Please enter 'y' if you achieved the correct answer and please enter 'n' if you achieved the incorrect answer:"))
        while User_ans != "n" and User_ans != "y":
            print("Please type in either 'y' or 'n'")
            User_ans = str(input(
                "Please enter 'y' if you achieved the correct answer and please enter 'n' if you achieved the incorrect answer:"))

        if User_ans == "y":
            Ans_Verify = True
            Count = Count + 1
            print("Well done you have 1 more point")
            print("Here is your current count: ", Count)
        elif User_ans == "n":
            Ans_Verify = False
            print("Don't worry just try again.")
    print("Here is your final count: ", Count)

def Menu():
   print("Welcome to Flashygame developed by Caseless Computing")
   print("""
         MENU

         1.1.1 Number representation
         1.1.2 Images 
         1.1.3 Sound
         1.1.4 Video
         1.1.5 Compression techniques
         1.2.1 Networks
         1.2.2 IP addressing
         1.2.3 Client- and server-side scripting
         1.3.1 Input, output and storage devices
         1.3.2 Main memory
         1.3.3 Logic gates and logic circuits
         1.4.1 CPU architecture
         1.4.2 The fetch-execute cycle
         1.4.3 The processor’s instruction set
         1.4.4 Assembly language
         1.5.1 Operating system
         1.5.2 Utility programs
         1.5.3 Library programs
         1.5.4 Language translators
         1.6.1 Data security
         1.6.2 Data integrity
         1.7.1 Ethics
         1.7.2 Ownership
         1.8.1 Database Management Systems (DBMS)
         1.8.2 Relational database modelling
         1.8.3 Data Defi nition Language (DDL) and Data Manipulation
   """)
   print("Enter subject number (e.g. 112 for images")
   userselect = input()
   if userselect == "111":
        #df
   elif userselect == "113":
        #df
   elif userselect == "114":
        # df
   elif userselect == "115":
        # df
   elif userselect == "121":
        AnsVerify()
   elif userselect == "122":
        # df
   elif userselect == "123":
        # df
   elif userselect == "131":
        # df
   elif userselect == "132":
        # df
   elif userselect == "133":
        # df
   elif userselect == "141":
        # df
   elif userselect == "142":
        # df
   elif userselect == "143":
        # df
   elif userselect == "144":
        # df
   elif userselect == "151":
        # df
   elif userselect == "152":
        # df
   elif userselect == "153":
        # df
   elif userselect == "154":
        # df
   elif userselect == "161":
        # df
   elif userselect == "162":
        # df
   elif userselect == "171":
        # df
   elif userselect == "172":
        # df
   elif userselect == "181":
        # df
   elif userselect == "182":
        # df
   elif userselect == "183":
        # df
   else:
      print("Please enter in correct format")
# df


Menu()