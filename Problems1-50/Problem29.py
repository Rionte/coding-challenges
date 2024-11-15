# Distinct Powers - 0.008879899978637695 seconds - ans: 9183

import time
start = time.time()

answers = []
for i in range(2, 100 + 1):
    for j in range(2, 100 + 1):
        answers.append(i ** j)
answers = list(dict.fromkeys(answers))
print(len(answers))

end = time.time()
print(end-start)