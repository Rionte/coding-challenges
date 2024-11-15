# Largest Palindrome Product - 983.8357651233673 seconds - ans: 906609

import time
start = time.time()

currentPal = 0
for i in range(100, 1000):
    for j in range(100,1000):
        num = str(i * j)
        firstHalf = num[:len(num)//2]
        secondHalf = num[len(num)//2:]
        if not(len(num) % 2 == 0):
            firstHalf = firstHalf + num[len(num)//2]
        if (firstHalf == secondHalf[::-1]) and (int(num) > currentPal):
            currentPal = int(num)
print(currentPal)

end = time.time()
print(end-start)