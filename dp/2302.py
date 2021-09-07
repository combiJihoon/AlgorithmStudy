import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
fixed = []
for _ in range(m):
    fixed.append(int(input()))

dp = [0] * 41
dp[0] = 1
dp[1] = 1
for i in range(2, 41):
    dp[i] = dp[i-1] + dp[i-2]

prev = 0
ans = 1
for i in range(m):
    ans *= dp[fixed[i] - prev - 1]
    prev = fixed[i]

ans *= dp[n-prev]

print(ans)
