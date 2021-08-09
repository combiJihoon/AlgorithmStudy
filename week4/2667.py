import sys
from collections import deque

input = sys.stdin.readline


def dfs(y, x):
    global cnt

    moves = [
        [1, 0],
        [-1, 0],
        [0, 1],
        [0, -1]
    ]
    for (dy, dx) in moves:
        ny = y + dy
        nx = x + dx
        if 0 <= ny <= n-1 and 0 <= nx <= m-1:
            if not visited[ny][nx] and arr[ny][nx] == 1:
                visited[ny][nx] = True
                cnt += 1
                dfs(ny, nx)


n = int(input())
arr = []
for _ in range(n):
    tmp = input().strip()
    arr.append(list(map(int, tmp)))

m = len(arr[0])
visited = [[0] * (m) for _ in range(n)]
# i : 세로, j : 가로
result = []
for i in range(n):
    for j in range(m):
        if not visited[i][j] and arr[i][j] == 1:
            visited[i][j] = True
            cnt = 1
            dfs(i, j)
            result.append(cnt)

print(len(result))
for i in sorted(result):
    print(i)


# def bfs(y, x):
#     moves = [
#         [1, 0],
#         [-1, 0],
#         [0, 1],
#         [0, -1]
#     ]
#     q = deque()
#     q.append((y, x))

#     while q:
#         y, x = q.popleft()

#         for (dy, dx) in moves:
#             ny = y + dy
#             nx = x + dx
#             if 0 <= ny <= n-1 and 0 <= nx <= m-1:
#                 if arr[ny][nx] == 1:
#                     arr[ny][nx] = arr[y][x] + 1
#                     q.append((ny, nx))
