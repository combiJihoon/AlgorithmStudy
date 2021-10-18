import sys

input = sys.stdin.readline
n, d, k, c = map(int, input().split())
arr = [int(input()) for _ in range(n)]

max_cnt = 0
for i in range(n):
    cnt = 0
    tmp = [0 for _ in range(d+1)]
    eaten = []
    for j in range(k):
        tmp[arr[(i+j) % n]] = 1  # 순환이기 때문에 나머지 구함
        eaten.append(arr[(i+j) % n])
    cnt += tmp.count(1)

    if c not in eaten:
        cnt += 1

    max_cnt = max(max_cnt, cnt)

print(max_cnt)
