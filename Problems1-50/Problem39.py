# Integer Right Triangles - x seconds - ans: y

def TriSolutions(n):
    solutions = 0
    for i in range(1, n + 1):
        for j in range(1, (n // i) + 1):
            if n % (i * j) == 0:
                k = n // (i * j)
                if i * j * k == n:
                    solutions += 1
    return solutions

print(TriSolutions(120))