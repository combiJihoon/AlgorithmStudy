import sys

input = sys.stdin.readline
k, n = map(int, input().split())
arr = [int(input()) for _ in range(k)]

s = 1
e = max(arr)
while s <= e:
    mid = (s+e) // 2
    tmp = 0
    for i in arr:
        tmp += i // mid
    if tmp >= n:
        s = mid + 1
    else:
        e = mid - 1
print(e)
