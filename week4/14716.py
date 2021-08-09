import sys
from collections import deque

input = sys.stdin.readline


def bfs(y, x):
    moves = [
        [0, -1],
        [0, 1],
        [-1, 0],
        [1, 0],
        [1, 1],
        [1, -1],
        [-1, 1],
        [-1, -1]
    ]
    q = deque()
    q.append((j, i))
    visited[j][i] = True

    while q:
        y, x = q.popleft()
        for move in moves:
            dy, dx = move
            ny = y + dy
            nx = x + dx
            if 0 <= ny <= n-1 and 0 <= nx <= m-1:
                if visited[ny][nx] == False:
                    if arr[ny][nx] == 1:
                        visited[ny][nx] = True
                        q.append((ny, nx))


# 세로, 가로
n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
visited = [[False] * m for _ in range(n)]
cnt = 0
for j in range(n):
    for i in range(m):
        if visited[j][i] == False and arr[j][i] == 1:
            bfs(j, i)
            cnt += 1
print(cnt)
