import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coins = []

for _ in range(n):
    coins.append(int(input()))
coins = list(reversed(coins))
val = 0
cnt = 0
left_val = k
for coin in coins:
    if coin <= left_val:
        cnt += left_val // coin
        left_val = left_val % coin
        if left_val == 0:
            break
print(cnt)
