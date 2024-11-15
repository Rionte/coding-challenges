# Pentagon Numbers - x seconds - ans: y

import time
start = time.time()

def GetPentaNum(n):
    return int((n * ((3 * n) - 1)) / 2)

def CheckPentaNum(p):
    n = (1 + ((1 - (24 * -p)) ** .5)) / 6
    if n.is_integer():
        return True
    return False

currentNum = 1
while 1:
    pentaOne = GetPentaNum(currentNum)
    for i in range(1, currentNum):
        pentaTwo = GetPentaNum(i)
        print(pentaOne - pentaTwo)
        if CheckPentaNum(pentaOne + pentaTwo) and CheckPentaNum(pentaOne - pentaTwo):
            print("p1:",pentaOne,"p2:",pentaTwo)
            break
    else:
        currentNum += 1
        continue
    break

end = time.time()
print(end-start)