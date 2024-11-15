# Multiples of 3 or 5 - 0.0010325908660888672 seconds - ans: 233168

import time
start = time.time()

sum = 0
for i in range(1,1000):
    if i % 3 == 0 or i % 5 == 0:
        sum += i

print(sum)

end = time.time()
print(end-start)