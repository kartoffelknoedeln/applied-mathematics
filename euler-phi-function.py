def isNumPrime(num):
    for i in range(num // 2, 1, -1):
        if num%i == 0:
            return False
    return True
    
def factors(num):
    i = num
    factorList = []
    for i in range(round(num/2), 1, -1):
        if num%i == 0:
            factorList += i,
    return factorList

def isFactorPrime(factorList):
    sortedList = []
    for i in range(len(factorList)):
        if isNumPrime(factorList[i]) == True:
            sortedList += factorList[i],
    return sortedList

def eulerphiFunction(num, sortedList, checkcheck):
    if checkcheck == True:
        print('The Euler-Phi function of', num, 'is', num-1)
    else:
        answer = num
        for i in range(len(sortedList)):
            faction = 1 - 1/sortedList[i]
            answer = answer*faction
        print('The Euler-Phi function of', num, 'is', int(answer))

def main():
    num = int(input('Enter a number: '))
    checkcheck = isNumPrime(num)
    factorList = factors(num)
    isFactorPrime(factorList)
    eulerphivalues = isFactorPrime(factorList)
    eulerphiFunction(num, eulerphivalues, checkcheck)

main()
