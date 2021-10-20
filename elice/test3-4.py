import sys

input = sys.stdin.readline
n = int(input())
xs = []
ys = []
for _ in range(n):
    i, j = map(int, input().split())
    xs.append(i)
    ys.append(j)

points = [0] * (max(xs)+1)
for i in range(n):
    x = xs[i]
    y = ys[i]
    if points[x] < y:
        points[x] = y


area = 0
x1, y1 = -1, -1
for i in range(len(points)):
    x, y = i, points[i]
    if x != 0 and y != 0:
        if x1 == -1 and y1 == -1:
            x1, y1 = x, y
        else:
            w = x - x1
            h1 = min(y1, y)
            h2 = max(y1, y) - h1
            area += (w * h1) + (w * h2) / 2
            x1, y1 = x, y

if round(area) != area:
    print(area)
else:
    print(int(area))
