# Summation of Primes - 47.86868858337402 seconds - ans: 142913828922

import time
start = time.time()

def CheckPrime(n):
    for i in range(2, int((n + 1) ** .5) + 1):
        if (n % i == 0) and (n != i):
            return False
    return True

primeList = []
for i in range(2, 2000000 + 1):
    if CheckPrime(i):
        primeList.append(i)

print(sum(primeList))

end = time.time()
print(end-start)