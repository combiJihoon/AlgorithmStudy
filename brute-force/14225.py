import sys
import heapq
from itertools import combinations as cb

input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))

save = set()
target = 1
i = 1
while i <= n:
    for case in list(cb(nums, i)):
        save.add(sum(case))
    i += 1

save = list(save)
heapq.heapify(save)
target = 1
while save:
    x = heapq.heappop(save)
    if x != target:
        print(target)
        break
    target += 1
else:
    print(target)
