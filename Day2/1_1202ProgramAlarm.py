import csv

def calculateIntcode(listOfIntegers):
    i = 0
    listOfIntegers[1] = 12
    listOfIntegers[2] = 2
    while(i < len(listOfIntegers)):
        opcode = listOfIntegers[i]
        # print(opcode)
        if(opcode == 1):
            index1 = listOfIntegers[i+1]
            index2 = listOfIntegers[i+2]
            result = listOfIntegers[index1] + listOfIntegers[index2]
            resultIndex = listOfIntegers[i+3]
            listOfIntegers[resultIndex] = result
        elif(opcode == 2):
            index1 = listOfIntegers[i+1]
            index2 = listOfIntegers[i+2]
            result = listOfIntegers[index1] * listOfIntegers[index2]
            resultIndex = listOfIntegers[i+3]
            listOfIntegers[resultIndex] = result
        elif(opcode == 99):
            return listOfIntegers
        else:
            print("Something Went Wrong")
        i = i+4
    return listOfIntegers

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
    print(calculateIntcode(listOfIntegers))


if __name__ == '__main__':
    main()
