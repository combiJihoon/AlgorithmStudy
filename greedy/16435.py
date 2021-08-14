import sys

input = sys.stdin.readline

n, l = map(int, input().split())
hs = sorted(list(map(int, input().split())))

cnt = 0
for h in hs:
    if h <= l:
        l += 1

print(l)
