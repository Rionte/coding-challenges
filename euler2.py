sequence = [1, 2]
currentIndex = 1

while sequence[currentIndex] < 4000000:
    sequence.append(sequence[currentIndex] + sequence[currentIndex - 1])
    currentIndex += 1

total = 0

for i in sequence:
    if i % 2 == 0:
        total += i
    
print(total)