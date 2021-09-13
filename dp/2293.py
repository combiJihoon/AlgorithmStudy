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
'''
<1>
1
<2>dp[i-1]+dp[i]=1+1=2
11
2
<3>dp[i-1]+dp[i]=2
111
12
<4>dp[i-1]+dp[i]=3
1111
112
22
<5>dp[i-1]+dp[i]=4
11111
1112
122
5
<6>5
111111
11112
1122
222
15

<7>6
1111111
111112
11122
1222
115
25

'''
