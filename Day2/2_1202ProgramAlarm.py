import csv

def calculateIntcode(listOfIntegers):
    listOfIntegers1 = listOfIntegers
    for i1 in range(0,100):
        for i2 in range(0,100):
            i = 0
            # print(i1,i2)
            tempListOfInteger = listOfIntegers1.copy()
            # print(listOfIntegers1)
            tempListOfInteger[1] = i1
            tempListOfInteger[2] = i2
            while(i < len(tempListOfInteger)):
                opcode = tempListOfInteger[i]
                # print(i)
                if(opcode == 1):
                    index1 = tempListOfInteger[i+1]
                    index2 = tempListOfInteger[i+2]
                    result = tempListOfInteger[index1] + tempListOfInteger[index2]
                    resultIndex = tempListOfInteger[i+3]
                    tempListOfInteger[resultIndex] = result
                elif(opcode == 2):
                    index1 = tempListOfInteger[i+1]
                    index2 = tempListOfInteger[i+2]
                    result = tempListOfInteger[index1] * tempListOfInteger[index2]
                    resultIndex = tempListOfInteger[i+3]
                    # print(i,"  resultIndex = ",resultIndex)
                    if(resultIndex <= len(tempListOfInteger)):
                        tempListOfInteger[resultIndex] = result
                    else:
                        break
                elif(opcode == 99):
                    # tempListOfInteger = tempListOfInteger
                    break
                else:
                    break
                    # print("Something Went Wrong")
                i = i+4
            # print(tempListOfInteger[0])
            if(tempListOfInteger[0] == 19690720):
                print("yes", i1,i2)
                return i1,i2

def main():
    file = open("dataFile.txt","r")
    i = 0
    listOfIntegers = []
    # listOfIntegers = [1,1,1,4,99,5,6,0,99]
    for line in file:
        currentline = line.split(",")
        for i in currentline:
            listOfIntegers.append(int(i))
    # print(listOfIntegers)
    noun,verb = calculateIntcode(listOfIntegers)
    print(100*noun + verb)


if __name__ == '__main__':
    main()
