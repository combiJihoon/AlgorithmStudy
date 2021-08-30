import sys

input = sys.stdin.readline

n = int(input())
pos_x = []
pos_y = []
for _ in range(n):
    x, y = map(int, input().split())
    pos_x.append(x)
    pos_y.append(y)

pos_x = sorted(pos_x)
pos_y = sorted(pos_y)

mid = n // 2
mid_x = pos_x[mid]
mid_y = pos_y[mid]

dist = 0
for i in range(n):
    dist += abs(pos_x[i] - mid_x) + abs(pos_y[i] - mid_y)

print(dist)
