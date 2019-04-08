import math

def primes(limit):
    sieve = [True] * limit
    primelist = []
    sieve[0] = False ## 1 is not a prime number
    sievelimit = round(math.sqrt(limit))
    
    for i in range(4, limit+1):
        for j in range(2, sievelimit+1):
            if i%j == 0 and i != j:
                sieve[i-1] = False
                
    ## set to index+1 because index starts at 0
    return [index+1 for index in range(len(sieve)) if sieve[index] == True]

def main():
    print(primes(100))

main()
