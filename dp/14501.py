import sys

input = sys.stdin.readline

n = int(input())
t = []
p = []
for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)
# n일차까지의 최대이익
dp = [0] * (n+1)
for i in range(n-1, -1, -1):
    if i+t[i] <= n:
        dp[i] = max(dp[i+1], p[i]+dp[i+t[i]])
    else:
        dp[i] = dp[i+1]

print(dp[0])
