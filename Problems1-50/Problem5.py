# Smallest Multiple - 210.20445084571838 seconds - ans: 232792560

import time
start = time.time()

def CheckMultiples(n):
    for i in range(1, 21):
        if n % i != 0:
            return False
    return True

num = 5
while 1:
    if CheckMultiples(num):
        break
    num += 5

print(num)

end = time.time()
print(end-start)