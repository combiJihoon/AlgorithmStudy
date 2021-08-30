import sys

input = sys.stdin.readline

n = int(input())
prices = []  # [3, 2, 3, 2]
for _ in range(n):
    prices.append(int(input()))
prices = sorted(prices)

is_three = 0
for i in range(n-1, -1, -1):
    is_three += 1
    if is_three % 3 == 0:
        prices[i] = 0
        is_three = 0
print(sum(prices))
