import sys

input = sys.stdin.readline

n, a, d = map(int, input().split())
notes = list(map(int, input().split()))

num = 0
cnt = 0
for i in range(len(notes)):
    if notes[i] == a + (d * num):
        cnt += 1
        num += 1

print(cnt)
