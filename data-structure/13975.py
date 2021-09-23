import sys
import heapq

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())

    chapters = list(map(int, input().split()))
    heapq.heapify(chapters)
    save = 0
    while len(chapters) > 1:
        x = heapq.heappop(chapters)
        y = heapq.heappop(chapters)
        heapq.heappush(chapters, x+y)
        save += (x+y)

    print(save)
