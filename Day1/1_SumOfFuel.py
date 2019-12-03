# Fuel required to launch a given module is based on its mass. Specifically,
# to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2

def calculateFuelRequired(mass):
    fuelRequired = int(mass/3) - 2
    return fuelRequired

def sumOfFuelRequired(listOfModules):
    sum = 0
    for i in range(len(listOfModules)):
        # print(str(i)+"  "  +str(listOfModules[i]))
        fuelForModule = calculateFuelRequired(listOfModules[i])
        sum = sum + fuelForModule
    return sum

def main():
    listOfModules = []
    file = open("dataFile.txt","r")
    for i in file:
        listOfModules.append(int(i))
    file.close()
    sum = sumOfFuelRequired(listOfModules)
    print(sum)

if __name__ == '__main__':
    main()
