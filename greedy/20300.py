import sys

input = sys.stdin.readline

n = int(input())
ts = sorted(list(map(int, input().split())))

max_sum = 0

if n % 2 == 0:
    for i in range(len(ts)//2):
        tmp = ts[i] + ts[len(ts)-1-i]
        max_sum = max(max_sum, tmp)
else:
    for i in range((len(ts)//2)-1):
        tmp = ts[i] + ts[len(ts)-2-i]
        max_sum = max(max_sum, tmp)
    max_sum = max(max_sum, ts[-1])
print(max_sum)
