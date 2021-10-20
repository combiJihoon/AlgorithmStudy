import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline
n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

picked = [1] * n


def find(x, cnt):
    if cnt == n:
        return
    if picked[x-1] == 1:
        picked[x-1] = 0
        find(arr[x-1][0], cnt+1)
        find(arr[x-1][1], cnt+1)


find(k, 0)
print(sum(picked))
