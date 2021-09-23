import sys
import heapq

input = sys.stdin.readline
n = int(input())

# n번째 수가 나오면 break
# 최대 힙에 넣는다.
hq = []
for _ in range(n):
    for x in list(map(int, input().split())):
        heapq.heappush(hq, x)
    while len(hq) > n:
        heapq.heappop(hq)

print(hq[0])
