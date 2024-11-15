# Highly Divisible Triangular Number - 14.606857538223267 seconds - ans: 76576500

import time
start = time.time()

def GetTriNum(n):
    triNum = (n * (n + 1)) / 2
    return int(triNum)

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
    while 1:
        for i in range(2, nextFactor + 1):
            if not CheckPrime(i) or (nextFactor % i != 0):
                continue
            primeFactors.append(i)
            nextFactor = nextFactor // i
            break
        if CheckPrime(nextFactor):
            primeFactors.append(nextFactor)
            break
    for i in primeFactors:
        expDict.update({i:primeFactors.count(i)})
    for i in expDict:
        numFactorCount = numFactorCount * (expDict[i] + 1)
    return numFactorCount

loopCount = 1
while 1:
    currentNum = GetTriNum(loopCount)
    factorCount = GetFactors(currentNum)
    if factorCount > 500:
        print(currentNum)
        break
    loopCount += 1

end = time.time()
print(end-start)