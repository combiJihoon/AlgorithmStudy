import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
length = n // m

dp = [-1] * n
dp[0] = arr[0]

# dp 구하기를 dfs로 반복하면 어떨까
max_val = -1
for i in range(1, n):
    dp[i] = max(dp[i], dp[i-1]+arr[i])
print(dp)

-1 3 1 2 4 - 1


def dfs(i):
    if i == n:
        return
    dp.append(i)
    dfs(i+1)
    dp.pop()


max_sum = -1
for i in range(1, n):
    max_sum = max(max_sum, dfs(i))
