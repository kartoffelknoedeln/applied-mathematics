def checkingByTwo(num):
    power = 0
    for i in range(1, 10):
        if (num - 1)%(2**i) == 0:
            power += 1
    compositepart = int(num/(2**power))
    return compositepart, power

def rabinMillerTest(num, compositepart, power, witness):
    for i in range(power):
        if (witness**((2**i)*compositepart)%num) != 1 and (witness**((2**i)*compositepart)%num) != num - 1:
            print('Witness', witness, 'with power', i, 'does not generate a number that is 1 or -1.')
        else:
            print('Witness', witness, 'with power', i, 'does generate a number that is 1 or -1.')

def main():
    num = int(input('Please enter a number to check if it is composite: '))
    witness = int(input('Please enter a number that is the witness: '))
    compositepart, power = checkingByTwo(num)
    rabinMillerTest(num, compositepart, power, witness)

main()
