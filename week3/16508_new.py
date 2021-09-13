import sys
from itertools import product as pd

# 입력
target = str(input()).strip()
n = int(input())
prices = []
titles = []
for _ in range(n):
    x, y = input().split()
    prices.append(int(x))
    titles.append(str(y))

cases = [i for i in pd([0, 1], repeat=n)]

# 글자 오려내기
