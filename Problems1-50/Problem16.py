# Power Digit Sum - 0.0009539127349853516 seconds - ans: 1366

import time
start = time.time()

ans = 0
num = str(2 ** 1000)
for i in num:
    ans += int(i)
print(ans)

end = time.time()
print(end - start)