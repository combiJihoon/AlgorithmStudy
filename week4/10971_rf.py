import sys

input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]


min_cost = int(1e9)


def dfs(start, next, visited, cost):
    global min_cost

    # base case
    if len(visited) == n:
        if arr[next][start] != 0:
            min_cost = min(min_cost, cost+arr[next][start])
        return

    for i in range(n):
        if arr[next][i] != 0 and i != start and i not in visited:
            visited.append(i)
            dfs(start, i, visited, cost+arr[next][i])
            visited.pop()


# 시작 지점 고르기
for i in range(n):
    visited = [i]
    dfs(i, i, visited, 0)
print(min_cost)
