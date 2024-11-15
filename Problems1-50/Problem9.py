# Special Pythagorean Triplet - 0.08984756469726562 seconds - ans: 31875000

import time
start = time.time()

for a in range(1, 999):
    for b in range(a, (1000 - 1 - a) + 1):
        c = (1000 - (a + b))
        if ((a**2) + (b**2)) == (c**2):
            print(a * b * c)
            break
    else:
        continue
    break        

end = time.time()
print(end-start)