import sys

input = sys.stdin.readline

n, l = map(int, input().split())
pos = sorted(list(map(int, input().split())))

result = 1
start = pos[0]
end = pos[0] + l

for p in pos:
    if start <= p < end:
        continue
    else:
        start = p
        end = p + l
        result += 1

print(result)
