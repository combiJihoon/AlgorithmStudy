import sys

input = sys.stdin.readline

INF = int(1e9)
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
# 1을 5배 한 값
dp = [[INF] * (1 << n) for _ in range(n)]


def dfs(x, v):
    if v == (1 << n) - 1:  # 모든 도시 방문
        if arr[x][0]:
            return arr[x][0]
        else:
            return INF

    if dp[x][v] != INF:  # 이미 최소 비용이 계산됨
        return dp[x][v]

    for i in range(1, n):
        if not arr[x][i]:  # 가는 경로 없으면 못감
            return
        if v & (1 << i):  # 방문한 도시면 skip
            continue
        dp[x][v] = min(dp[x][v], dfs(i, v | (1 << i) + arr[x][i]))
    return dp[x][v]


print(dfs(0, 1))
