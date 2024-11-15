# Amicable Numbers - 13.527647972106934 seconds - ans: 40284

import time
start = time.time()

def SumOfDivs(n):
    divs = []
    for i in range(1, (n // 2) + 1):
        if n % i == 0:
            divs.append(i)
    sum = 0
    for i in divs:
        sum += i
    return sum

def CheckAmicable(n): 
    if n == SumOfDivs(SumOfDivs(n)):
        return True
    return False

sum = 0
for i in range(1, 10000 + 1):
    if CheckAmicable(i):
        print(i)
        sum += i
print(sum)

end = time.time()
print(end-start)