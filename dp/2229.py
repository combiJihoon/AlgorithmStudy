import sys

input = sys.stdin.readline

n = int(input())
scores = list(map(int, input().split()))
dp = [0] * (n+1)

for i in range(1, n+1):
    h = -1
    l = int(1e9)
    for j in range(i-1, -1, -1):
        h = max(h, scores[j])
        l = min(l, scores[j])
        dp[i] = max(dp[i], dp[j] + (h - l))
print(dp[-1])
