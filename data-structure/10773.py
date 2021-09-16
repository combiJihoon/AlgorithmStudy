import sys
from collections import deque

input = sys.stdin.readline

k = int(input())
q = deque()
for _ in range(k):
    q.append(int(input()))

nums = []
while q:
    x = q.popleft()
    if x != 0:
        nums.append(x)
    else:
        nums.pop()
print(sum(nums))
