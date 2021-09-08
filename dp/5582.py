import sys

input = sys.stdin.readline

s = str(input().strip())
t = str(input().strip())

dp = [[0] * (len(t)+1) for _ in range(len(s)+1)]

ans = 0
for i in range(1, len(s)+1):
    for j in range(1, len(t)+1):
        if s[i-1] == t[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
            ans = max(ans, dp[i][j])

print(ans)
