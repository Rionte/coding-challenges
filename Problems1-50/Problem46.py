# Goldbach's Other Conjecture - 2.4992899894714355 seconds - ans: 5777

import time
start = time.time()

def CheckComposite(n):
    for i in range(2, int((n + 1) ** .5) + 1):
        if (n % i == 0) and (n != i):
            return True
    return False

currentNum = 3
while 1:
    solutionFound = False
    if CheckComposite(currentNum):
        for i in range(2, currentNum):
            if not CheckComposite(i):
                if (((currentNum - i) / 2) ** .5).is_integer():
                    #print("num:",currentNum,"prime:",i,"squ:",(((currentNum - i) / 2) ** .5))
                    solutionFound = True
                    break
        if not solutionFound:
            print(currentNum)
            break
    currentNum += 2

end = time.time()
print(end-start)