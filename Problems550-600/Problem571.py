# Super Pandigital Numbers - x seconds - ans: y

import time
start = time.time()

bases = []
num = 0
numSuperPans = 0
sumSuperPans = 0
superPans = []

def base10Convert(num):
    for i in range(2,11):
        currentBase = i
        currentBaseDigs = []
        currentWorkingDig = 0
        workingNum = num
        while workingNum != 0:
            currentWorkingDig = workingNum % currentBase
            currentBaseDigs.append(currentWorkingDig)
            workingNum = workingNum // currentBase
        currentBaseDigs.reverse()
        bases.append(currentBaseDigs)

def checkSuperPan(baseList):
    isSuperPan = False
    for idx, i in enumerate(baseList[::-1]):
        if all(j in i for j in range(0,idx+2)):
            isSuperPan = True
        else:
            isSuperPan = False
            break
    return(isSuperPan)
    
print(checkSuperPan(base10Convert(1093265784)))
while 1:
    num += 1
    base10Convert(num)
    if checkSuperPan(bases):
        print(num,"test")
        numSuperPans += 1
        sumSuperPans += num
        superPans.append(num)
        if numSuperPans == 10:
            break

print(numSuperPans)
print(sumSuperPans)
print(superPans)

end = time.time()
print(end-start)

#check if 10-pan works
#optimize
#find 12-pan