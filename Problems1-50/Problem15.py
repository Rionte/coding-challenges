# Lattice Paths - 0.0007309913635253906 seconds - ans: 137846528820

import time
start = time.time()

def Factorial(n):
    ans = 1
    for i in range(2, n + 1):
        ans = ans * i
    return ans

def NumRoutes(size):
    n = size * 2
    k = size
    return (Factorial(n)) // (Factorial(k) * Factorial(n - k))

print(NumRoutes(20))

end = time.time()
print(end-start)