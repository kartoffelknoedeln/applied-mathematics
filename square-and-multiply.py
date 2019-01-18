def isNumPrime(modulo):
    for i in range(round(modulo/2), 1, -1):
        if modulo%i == 0:
            return False
    return True
    
def factors(modulo):
    i = modulo
    factorList = []
    for i in range(round(modulo/2), 1, -1):
        if modulo%i == 0:
            factorList += i,
    return factorList

def isFactorPrime(factorList):
    sortedList = []
    for i in range(len(factorList)):
        if isNumPrime(factorList[i]) == True:
            sortedList += factorList[i],
    return sortedList

def eulerphiFunction(modulo, sortedList, checkcheck):
    if checkcheck == True:
        eulerphianswer = modulo-1
        return eulerphianswer
    else:
        eulerphianswer = modulo
        for i in range(len(sortedList)):
            faction = 1 - 1/sortedList[i]
            eulerphianswer = eulerphianswer*faction
        return eulerphianswer

def powersBreakdown(power, eulerphianswer):
    num = int(power - eulerphianswer)
    powers = []
    i = 1
    while i <= num:
        if i & num:
            powers.append(i)
        i <<= 1
    return powers

def powersMultiply(powers, base, modulo):
    x = 1
    for i in range(len(powers)):
        x = x*(base**powers[i])
    print('The answer is', x%modulo)

def main():
    print('Welcome to the square and multiple algorithm.')
    base = int(input('Enter the base number: '))
    power = int(input('Enter the power number: '))
    modulo = int(input('Enter the modulo number: '))
    checkcheck = isNumPrime(modulo)
    factorList = factors(modulo)
    isFactorPrime(factorList)
    eulerphivalues = isFactorPrime(factorList)
    eulerphianswer = eulerphiFunction(modulo, eulerphivalues, checkcheck)
    powers = powersBreakdown(power, eulerphianswer)
    powersMultiply(powers, base, modulo)

main()
