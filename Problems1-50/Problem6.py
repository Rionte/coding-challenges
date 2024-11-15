# Sum Square Difference - 0.0019254684448242188 seconds - ans: 25164150

import time
start = time.time()

numList = []
def CreateList(n):
    for i in range(1, n + 1):
        numList.append(i)
    return numList

CreateList(100)
sumOfSquares = sum(i ** 2 for i in numList)
squareOfSums = sum(numList) ** 2

print(squareOfSums - sumOfSquares)

end = time.time()
print(end-start)