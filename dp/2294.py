import sys

input = sys.stdin.readline
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp = [int(1e9)] * 100001
dp[0] = 0
for coin in coins:
    dp[coin] = 1

for i in range(1, k+1):
    for j in range(i+1):
        dp[i] = min(dp[i], dp[i-j]+dp[j])

if dp[k] == int(1e9):
    print(-1)
else:
    # print(dp[:k+1])
    print(dp[k])
