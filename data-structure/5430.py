# 마지막에는 리스트를 '뒤집어서 정렬'이 아니라 단순히 '뒤집어야' 한다.
import sys
from collections import deque

input = sys.stdin.readline
n = int(input())


# R: -1, D: 양수
def sol(arr, n, p):
    q = deque()
    for i in arr:
        q.append(i)

    R_flag = False

    for i in p:
        if i == 'R':
            if R_flag:
                R_flag = False
            else:
                R_flag = True
        else:
            if not q and n >= 0:
                return 'error'

            if R_flag:
                q.pop()
            else:
                q.popleft()
            n -= 1

    ans = list(q)
    if '' in ans:
        return []

    if R_flag:
        ans = list(map(str, ans))[::-1]
        return "["+",".join(ans)+"]"
    else:
        return "["+",".join(ans)+"]"


for _ in range(n):
    p = str(input().strip())
    n = int(input())
    tmp = input().strip()
    tmp = tmp.replace('[', '')
    tmp = tmp.replace(']', '')
    if len(tmp) > 0:
        tmp = tmp.split(',')
    ans = sol(tmp, n, p)
    print(ans)


# RDD
# 4
# [1, 2, 3, 4]
# 결과 : [2, 1]
