# Factorial Digit Sum - 0.0012710094451904297 seconds - ans: 648

import time
start = time.time()

def Factorial(n):
    ans = 1
    for i in range(2, n + 1):
        ans = ans * i
    return ans

num = 0
for i in str(Factorial(100)):
    num += int(i)
print(num)

end = time.time()
print(end-start)