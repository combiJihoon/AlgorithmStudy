import sys

input = sys.stdin.readline
n, h = map(int, input().split())
arr = sorted([list(map(int, input().split())) for _ in range(n)])

stop, cnt = -1, 0
for x, s, k in arr:
    if s > h:
        if k == 3:
            stop = x
            break
        if k == 1:
            cnt += 1

print(stop, cnt)
