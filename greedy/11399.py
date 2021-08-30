import sys

input = sys.stdin.readline

n = int(input())
times = sorted(list(map(int, input().split())))

result = 0
for t in times:
    result += t * n
    n -= 1
print(result)
