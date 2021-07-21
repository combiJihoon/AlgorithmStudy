import sys
import heapq

input = sys.stdin.readline
n = int(input())

hq = []

for i in range(n):
    x = int(input())
    if x == 0:
        if not hq:
            print(0)
        else:
            print(-heapq.heappop(hq))
    else:
        heapq.heappush(hq, -x)
