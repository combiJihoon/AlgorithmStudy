import sys

input = sys.stdin.readline

t = int(input())

results = []
for _ in range(t):
    n = int(input())
    x = str(input())
    y = str(input())

    w = 0
    b = 0
    for i in range(n):
        if x[i] != y[i]:
            if y[i] == 'W':
                w += 1
            elif y[i] == 'B':
                b += 1
    results.append(max(w, b))

for result in results:
    print(result, end="\n")
