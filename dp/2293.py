'''
어떻게 더해서 현재의 내 값으로 오게 되었는 지를 생각하면
당연히 빼야 한다는 것을 알 수 있다.
'''

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

# 다 더해서 k가 되는 경우의 수
dp = [0] * (k+1)
dp[0] = 1

for i in coins:
    for j in range(i, k+1):
        if j - i >= 0:
            dp[j] += dp[j-i]

print(dp[k])
