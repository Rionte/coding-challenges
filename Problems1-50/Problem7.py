# 10001st Prime - 1.0872094631195068 seconds - ans: 104743

import time
start = time.time()

def CheckPrime(n):
    for i in range(2, int((n + 1) ** .5) + 1):
        if (n % i == 0) and (n != i):
            return False
    return True

currentNum = 2
primeCount = 0
while 1:
    if CheckPrime(currentNum):
        primeCount += 1
        if primeCount == 10001:
            break
    currentNum += 1

print(currentNum)

end = time.time()
print(end-start)