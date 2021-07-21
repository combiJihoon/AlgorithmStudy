import sys

input = sys.stdin.readline

n, m = map(int, input().split())
strings = {input().rstrip() for _ in range(n)}
cnt = 0

for _ in range(m):
    string = input().rstrip()
    if string in strings:
        cnt += 1

print(cnt)
