#25/04/18 Pre release task 4 Cole Samson

maleSalary = [0,0,0,0,0]
femaleSalary = [0,0,0,0,0]

file = open('salaries.txt', 'r')

c = file.readline()
while len(c) > 0:
    # extract name
    endPos = c.find(',')
    thisName = c[0:endPos]
    c = c[endPos+1:]
    #print(thisName)
    # extract gender
    endPos = c.find(',')
    thisGender = c[1:endPos]
    c = c[endPos + 1:]
    print(thisGender)
    # extract salary
    thisSalary = float(c)
    print(str(thisSalary))
    # work out the salary category
    baseSum = 0.0
    index = 0
    elementID = -1
    while (baseSum < 110000.0) and (elementID == -1):
        if thisSalary <= 110000.0:
            if (baseSum <= thisSalary < (baseSum + 25000.0)):
            #if (thisSalary >= baseSum) and (thisSalary < (baseSum + 25000.0)):
                elementID = index
            else:
                baseSum = baseSum + 25000.0
                index = index + 1
        else:
            print('Salary outwith salary cap. Check source data.')
            break;
    print(elementID)

    # put in correct array by gender
    if (thisGender =='M'):
        maleSalary[elementID] += 1
    elif (thisGender=='F'):
        femaleSalary[elementID] += 1
    else:
        print('Gender error. Check source data.')
    # read next line
    c = file.readline()

print("{0:20}".format("Salary"),"M","\t","F")

baseSum = 0.0
index = 0
while (index <= 4):
    upper = baseSum + 25000.0
    if upper == 125000.0:
        upper = 110000.0
    message = str(str(baseSum) + "-" + str(upper) + "k")
    print("{0:20}".format(message),maleSalary[index],"\t",femaleSalary[index])

    index = index + 1
    baseSum += 25000.0


file.close()