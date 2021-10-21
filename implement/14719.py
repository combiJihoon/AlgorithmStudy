import sys

input = sys.stdin.readline
h, w = map(int, input().split())
arr = list(map(int, input().split()))

tot = 0
for i in range(w):
    max_left = max(arr[:i+1])
    max_right = max(arr[i:])
    if min(max_left, max_right) - arr[i] > 0:
        tot += min(max_left, max_right) - arr[i]

print(tot)
