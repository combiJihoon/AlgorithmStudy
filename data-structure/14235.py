import sys
import heapq

input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# 최대 힙
save = []
for case in arr:
    if case[0] == 0:
        if not save:
            print(-1)
        else:
            print(-(heapq.heappop(save)))
    else:
        for i in case[1:]:
            heapq.heappush(save, -i)
