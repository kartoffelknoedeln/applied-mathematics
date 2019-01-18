def findingGamma(modulo):
    gamma = 0
    while gamma**2 <= modulo:
        gamma += 1
    return gamma

def reversingPowers(base, gamma, modulo, answer):
    numlist = []
    for i in range(gamma-1):
        numlist += (answer*(base**(modulo-1-(i*gamma))))%37,
    return numlist

def listNumCheck(numlist, gamma):
    for i in range(len(numlist)):
        for j in range(1, gamma-1):
            if numlist[i] == 2**j:
                print('The answer is', i*gamma + j)
def main():
    print('This is the baby-step giant-step method to find the discrete log.')
    base = int(input('Enter the base number: '))
    modulo = int(input('Enter the modulo number: '))
    answer = int(input('Enter the answer number: '))
    gamma = findingGamma(modulo)
    numlist = reversingPowers(base, gamma, modulo, answer)
    listNumCheck(numlist, gamma)

main()
