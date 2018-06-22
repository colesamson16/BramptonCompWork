NumOfLine=0
def FileReader(NumOfLine):
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

    for line in file.readlines():
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

        return

    # each array is assigned its value of the fragmented string

    print(Section)
    print(Question)
    print(Answer)

    # Array values are printed out
FileReader()
print(NumOfLine)