# Largest Prime Factor - 0.01362466812133789 seconds - ans: 6857

import time
start = time.time()

def CheckPrime(n):
    for i in range(2, int((n + 1) ** .5) + 1):
        if (n % i == 0) and (n != i):
            return False
    return True

def GetFactors(n):
    nextFactor = n
    primeFactors = []
    expDict = {}
    numFactorCount = 1
    while True:
        for i in range(2, nextFactor + 1):
            if not CheckPrime(i) or (nextFactor % i != 0):
                continue
            primeFactors.append(i)
            nextFactor = nextFactor // i
            break
        if CheckPrime(nextFactor):
            primeFactors.append(nextFactor)
            break
    return max(primeFactors)

print(GetFactors(600851475143))

end = time.time()
print(end-start)