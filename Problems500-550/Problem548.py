# Gozinta Chains - x seconds - ans: y

import time
start = time.time()

factors = []
chains = []
totalChains = 1

for l in range(2,(10**16)+1):
    numChains = 0
    for i in range(2,l+1):
        if l % i == 0:
            factors.append(i)

    while 1:
        currentChain = [1]
        for i in factors:
            if i % currentChain[-1] == 0:
                if len(chains) > 0:
                    if all(i != j[-2] for j in [k for k in chains if k[0:-2] == currentChain]):
                        currentChain.append(i)
                else:
                    currentChain.append(i)
        chains.append(currentChain[:])
        currentChain.clear()
        if chains[-1] == [1,l]:
            break

    numChains = len(chains)
    chains.clear()
    factors.clear()
    if numChains == l:
        totalChains += numChains
        print(l, ":", numChains)
    
print(totalChains)

end = time.time()
print(end-start)