import sys
from itertools import combinations as cb

input = sys.stdin.readline

n = int(input())
items = sorted(list(map(int, input().split())))

if n % 2 == 0:
    print(sum(items[(n // 2):]) * 2)
else:
    print(items[n // 2] + sum(items[(n // 2) + 1:]) * 2)
