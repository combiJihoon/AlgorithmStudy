import sys

input = sys.stdin.readline

n = int(input())
boxes = list(map(int, input().split()))

# 나 자신의 개수도 포함이어서 +1이다.
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if boxes[i] > boxes[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
