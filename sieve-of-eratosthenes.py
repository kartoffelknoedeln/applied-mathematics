def primes(limit):
    sieve = [True] * limit
    sieve[0], sieve[1] = False, False

    num = 2
    while num < limit:
        while num < limit and not sieve[num]:
            num += 1
        for index in range(2*num, limit, num):
            sieve[index] = False
        num += 1
                
    return [index for index in range(len(sieve)) if sieve[index] == True]

def main():
    print(primes(100))

main()
