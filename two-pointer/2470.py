import sys

input = sys.stdin.readline

n = int(input())

arr = sorted(list(map(int, input().split())))

s = 0
e = n - 1
ans = []
min_ans = sys.maxsize

while s < e:
    tmp = arr[s] + arr[e]
    if abs(tmp) < min_ans:
        min_ans = abs(tmp)
        ans = [arr[s], arr[e]]

    if tmp >= 0:
        e -= 1
    else:
        s += 1

print(*ans)
