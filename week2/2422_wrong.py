import sys
from itertools import combinations as cb


input = sys.stdin.readline
n, m = map(int, input().split())

# cond = [(1, 2), (3, 4), (1, 3)]
condition = []
for i in range(m):
    x, y = map(int, input().split())
    tmp = str(x) + str(y)
    condition.append(tmp)

# 3가지 선택
icecream_list = [i for i in range(1, n+1)]
# [(1, 2, 3), (1, 2, 4),...]
combinated_icecream = []
combinated_icecream += cb(icecream_list, 3)

new_icecream = []
for icecream in combinated_icecream:
    tmp = ''
    for i in range(3):
        tmp += str(icecream[i])
    new_icecream.append(tmp)

i = 0
while i < len(new_icecream):
    for cond in condition:
        cnt = 0
        for c in cond:
            if c in new_icecream[i]:
                cnt += 1
        if cnt == 2:
            new_icecream[i] = ''
            break
    i += 1


print(len(new_icecream)-new_icecream.count(''))
# print(new_icecream)
# print(condition)
