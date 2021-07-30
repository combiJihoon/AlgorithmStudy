# 시간초과 해결...

import sys
# from copy import deepcopy

input = sys.stdin.readline
n, m = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()


stack = []
result = dict()
visited = [False] * n


def dfs():
    global num_list
    global result

    if len(stack) == m:
        tmp = " ".join(map(str, stack))
        # 시간초과 해결 위해 dict로 바꿈
        if tmp not in result:
            result[tmp] = True
            print(tmp)
            return

    for i in range(len(num_list)):
        # 중복 해결 위해 visited 넣음
        if not visited[i]:
            visited[i] = True
            stack.append(num_list[i])
            dfs()
            visited[i] = False
            stack.pop()


dfs()
