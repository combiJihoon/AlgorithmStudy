import sys

input = sys.stdin.readline
n = int(input())
arr = sorted([tuple(map(int, input().split())) for _ in range(n)])

start, end = arr[0][0], arr[0][1]
length = 0
for x, y in arr:
    if x > end:
        length += (end - start)
        start = x
        end = y
        continue
    end = max(y, end)
length += (end - start)
print(length)
