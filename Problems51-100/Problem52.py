# Permuted Multiples - 0.7785396575927734 seconds - ans: 142857

import time
start = time.time()

def GetDigits(n, multiple):
    newNum = n * multiple
    return sorted(str(newNum))

num = 1
while 1:
    if GetDigits(num, 2) == GetDigits(num, 3) == GetDigits(num, 4) == GetDigits(num, 5) == GetDigits(num, 6):
        break
    num += 1
print(num)

end = time.time()
print(end-start)