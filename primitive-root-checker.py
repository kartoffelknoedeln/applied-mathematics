def moduloFunction(primroot, modulo):
    remainderList = []
    for i in range(modulo - 1):
        remainderList += ((primroot**i) % modulo),
    remainderList.sort()
    return remainderList

def listChecker(sortedlist, modulo):
    counter = 1
    for i in range(modulo - 1):
        if sortedlist[i] == i + 1:
            counter += 1
    return counter

def counterChecker(counter, primroot, modulo):
    if counter == modulo:
        print(primroot, 'is a primitive root of', modulo)
    else:
        print(primroot, 'is not a primitive root of', modulo)

def main():
    primroot = int(input('Enter the primitive root: '))
    modulo = int(input('Enter the modulo: '))
    moduloFunction(primroot, modulo)
    sortedlist = moduloFunction(primroot, modulo)
    listChecker(sortedlist, modulo)
    counter = listChecker(sortedlist, modulo)
    counterChecker(counter, primroot, modulo)

main()
