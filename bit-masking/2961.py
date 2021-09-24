import sys
from itertools import combinations as cb

input = sys.stdin.readline
n = int(input())
sour = []
bitter = []
for _ in range(n):
    x, y = map(int, input().split())
    sour.append(x)
    bitter.append(y)

diff = int(1e9)
pick = n
while pick > 0:
    cb_list = list(cb([i for i in range(n)], pick))

    for case in cb_list:
        s = 1
        b = 0
        for c in case:
            s *= sour[c]
            b += bitter[c]
        diff = min(diff, abs(s-b))
    pick -= 1

print(diff)
