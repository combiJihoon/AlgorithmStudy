import sys
from collections import deque

input = sys.stdin.readline
t = int(input())


def sol():
    v = [0] * (n+1)
    cnt = 0
    q = deque()
    q.append(1)
    v[1] = 1

    while q:
        x = q.popleft()
        for i in arr[x]:
            if v[i] == 0:
                v[i] = 1
                cnt += 1
                if sum(v) != n:
                    q.append(i)
    return cnt


for _ in range(t):
    n, m = map(int, input().split())
    arr = [[] for _ in range(n+1)]
    for _ in range(m):
        x, y = map(int, input().split())
        arr[x].append(y)
        arr[y].append(x)
    print(sol())
