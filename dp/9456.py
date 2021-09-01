import sys

input = sys.stdin.readline


def sol(dp):
    dp[0][1] += dp[1][0]
    dp[1][1] += dp[0][0]

    # 대각선의 최댓값 또는 대각선 왼쪽의 최댓값
    for i in range(2, n):
        dp[0][i] += max(dp[1][i-2], dp[1][i-1])
        dp[1][i] += max(dp[0][i-2], dp[0][i-1])

    return max(dp[0][-1], dp[1][-1])


t = int(input())
for _ in range(t):
    n = int(input())
    dp = []
    for _ in range(2):
        dp.append(list(map(int, input().split())))
    if n == 1:
        print(max(dp[0][0], dp[1][0]))
    else:
        print(sol(dp))
