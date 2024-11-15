# Even Fibonacci Numbers - 0.0009496212005615234 seconds - ans: 4613732

import time
start = time.time()

num1 = 1
num2 = 2
sum = 2
while 1:
    nextNum = num1 + num2
    if nextNum > 4000000:
        break
    if nextNum % 2 == 0:
        sum += nextNum
    num1 = num2
    num2 = nextNum
print(sum)

end = time.time()
print(end-start)