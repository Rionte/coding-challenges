# Self Powers - 0.0223848819732666 seconds - ans: 9110846700

import time
start = time.time()

numList = []
for i in range(1, 1001):
    numList.append(i)

numPowerList = [i**i for i in numList]
print(str(sum(numPowerList))[-10:])

end = time.time()
print(end-start)