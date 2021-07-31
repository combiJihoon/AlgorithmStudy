import sys
from itertools import permutations as pm


input = sys.stdin.readline

n, k = map(int, input().split())
kits = list(map(int, input().split()))

# 키트 번호(인덱스)에 대한 조합
pm_kits = list(pm([i for i in range(n)], n))

cnt = 0
for case in pm_kits:
    health = 500
    is_increasing = True
    for i in case:
        # tmp : 증가량과 감소량의 차이
        tmp = kits[i] - k
        health += tmp
        if health < 500:
            is_increasing = False
            break
    if is_increasing:
        cnt += 1

print(cnt)
