# Triangular, Pentagonal, and Hexagonal - 0.10986042022705078 seconds - ans: 1533776805

import time
start = time.time()

def GetTriNum(n):
    return int((n * (n + 1)) / 2)

def CheckPentaNum(p):
    n = (1 + ((1 - (24 * -p)) ** .5)) / 6
    if n.is_integer():
        return True
    return False

def CheckHexaNum(h):
    n = (1 + ((1 - (8 * -h)) ** .5)) / 4
    if n.is_integer():
        return True
    return False

currentNum = 40755 + 1
while 1:
    triNum = GetTriNum(currentNum)
    if CheckPentaNum(triNum) and CheckHexaNum(triNum):
        print(triNum)
        break
    currentNum += 1

end = time.time()
print(end-start)