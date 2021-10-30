import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = sorted([list(map(int, input().split())) for _ in range(n)])

    cnt = 1
    cur = arr[0]
    for case in arr[1:]:
        if cur[1] > case[1]:
            cnt += 1
            cur = case

    print(cnt)
