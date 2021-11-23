import sys

input = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))

l, r = 0, 0
length = int(1e9)
tmp_sum = 0
while True:
    if tmp_sum >= s:
        length = min(length, r-l)
        tmp_sum -= arr[l]
        l += 1  # 범위 줄이기
    elif r == n:
        break
    else:
        tmp_sum += arr[r]
        r += 1  # 범위 늘리기

print(0 if length == int(1e9) else length)
