def checkingByTwo(num):
    power = 0
    for i in range(1, 10):
        if (num - 1)%(2**i) == 0:
            power += 1
    compositepart = int(num/(2**power))
    return compositepart, power

def rabinMillerTest(num, compositepart, power):
    counter = 0
    for i in range(power):
        if (2**((2**i)*compositepart)%num) != 1 and (2**((2**i)*compositepart)%num) != num - 1 and (3**((2**i)*compositepart)%num) != 1 and (3**((2**i)*compositepart)%num) != num - 1 and (5**((2**i)*compositepart)%num) != 1 and (5**((2**i)*compositepart)%num) != num - 1:
            counter += 1
    return counter

def compositeOrNot(num, counter, power):
    if counter >= 0.6*power:
        print(num, 'is probably a composite.')
    else:
        print(num, 'is probably a prime.')

def main():
    print('We will be using 2, 3, and 5 as witnesses.')
    num = int(input('Please enter a number to check if it is composite: '))
    compositepart, power = checkingByTwo(num)
    counter = rabinMillerTest(num, compositepart, power)
    compositeOrNot(num, counter, power)

main()
