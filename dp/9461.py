import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())

    dp = [1, 1, 1]

    if n >= 3:
        dp += [0] * (n - 3)

        for i in range(3, n):
            dp[i] = dp[i-2] + dp[i-3]
        print(dp[-1])
    else:
        print(dp[n])
