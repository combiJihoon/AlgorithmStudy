import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())
arr = [[] for _ in range(n+1)]
for i in range(m):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)


def bfs():
    visited = [0] * (n+1)
    q = deque()
    q.append(1)
    visited[1] = 1

    while q:
        x = q.popleft()
        for i in arr[x]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)

    print(visited.count(1) - 1)


bfs()


'''
dfs 풀이

def dfs(cur, visited):
    if cur == n+1:
        return
    tmp = arr[cur]
    for t in tmp:
        if visited[t] == 0:
            visited[t] = 1
            dfs(t, visited)


visited = [0] * (n+1)
visited[1] = 1
dfs(1, visited)

print(sum(visited) - 1)
'''
