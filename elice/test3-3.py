import sys

input = sys.stdin.readline
n = int(input())
arr = sorted([list(map(int, input().split()))
             for _ in range(n)], key=lambda x: x[0])

area = 0
x1, y1 = arr[0][0], arr[0][1]
for x, y in arr[1:]:
    w = x - x1
    h1 = min(y1, y)
    h2 = max(y1, y) - h1
    area += (w * h1) + (w * h2) / 2
    x1, y1 = x, y

if round(area) != area:
    print(area)
else:
    print(int(area))
