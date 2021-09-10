import sys

input = sys.stdin.readline

n = int(input())
one, two = list(map(int, input().split()))
m = int(input())
order = [int(input()) for _ in range(m)]

ans = int(1e9)


def dfs(one, two, depth, cnt):
    global ans

    if depth == m:
        ans = min(ans, cnt)
        return

    tmp1 = abs(one - order[depth])
    tmp2 = abs(two - order[depth])

    dfs(order[depth], two, depth+1, cnt+tmp1)
    dfs(one, order[depth], depth+1, cnt+tmp2)


dfs(one, two, 0, 0)
print(ans)
