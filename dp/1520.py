import sys

input = sys.stdin.readline


# 내리막으로만 내려간다.
def dfs(x, y):
    if x == m-1 and y == n-1:
        return 1
    moves = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    if dp[x][y] == -1:
        dp[x][y] = 0
        for dx, dy in moves:
            nx = x + dx
            ny = y + dy
            if 0 <= nx <= m-1 and 0 <= ny <= n-1:
                if arr[nx][ny] < arr[x][y]:
                    dp[x][y] += dfs(nx, ny)
    return dp[x][y]


m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]

dp = [[-1]*n for _ in range(m)]
print(dfs(0, 0))
