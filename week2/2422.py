import sys
from itertools import combinations as cb


input = sys.stdin.readline
n, m = map(int, input().split())

arr = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    arr[x][y] = 1
    arr[y][x] = 1


icecream = [i for i in range(1, n+1)]

cb_icecream = []
cb_icecream += cb(icecream, 3)

cnt = 0
for icecream in cb_icecream:
    is_possible = True
    for i in range(len(icecream)-1):
        for j in range(i+1, len(icecream)):
            x = icecream[i]
            y = icecream[j]
            if arr[x][y] == 1 and arr[y][x] == 1:
                is_possible = False
                break
        if not is_possible:
            break
    if is_possible:
        cnt += 1

print(cnt)
