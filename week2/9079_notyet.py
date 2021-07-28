import sys

input = sys.stdin.readline

n = int(input())
coins = []
for _ in range(n):
    tmp = []
    for i in range(3):
        tmp.append(list(map(str, input().split())))
    coins.append(tmp)

# 대각선 인덱스 :(0, 1, 2), (0, 1, 2)
