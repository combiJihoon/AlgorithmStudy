# 풀이 참고함...
# https: // jjangsungwon.tistory.com/4

import sys
from itertools import permutations as pm

input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

min_cost = int(1e9)


def dfs(start, next, visited, cost):
    global min_cost

    if len(visited) == n:
        if arr[next][start] != 0:
            min_cost = min(min_cost, cost+arr[next][start])
        return

    for i in range(n):
        if i not in visited and arr[next][i] != 0:
            # min_cost보다 큰 경우는 무시해야 시간초과 받지 않음
            if cost+arr[next][i] > min_cost:
                continue
            else:
                visited.append(i)
                dfs(start, i, visited, cost+arr[next][i])
                visited.pop()


for i in range(n):
    visited = [i]
    dfs(i, i, visited, 0)
print(min_cost)
