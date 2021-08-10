import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    # 세로, 가로 이동
    moves = [
        [1, 0, 0],
        [-1, 0, 0],
        [0, 1, 0],
        [0, -1, 0],
        [0, 0, 1],
        [0, 0, -1]
    ]
    while q:
        x, y, z = q.popleft()
        for (dx, dy, dz) in moves:
            nx = x + dx
            ny = y + dy
            nz = z + dz
            if 0 <= nx <= m-1 and 0 <= ny <= n-1 and 0 <= nz <= h-1:
                if arr[nz][ny][nx] == 0:
                    arr[nz][ny][nx] = arr[z][y][x] + 1
                    q.append((nx, ny, nz))


# 가로, 세로, 높이
m, n, h = map(int, input().split())

arr = []
for _ in range(h):
    tmp = []
    for _ in range(n):
        tmp.append(list(map(int, input().split())))
    arr.append(tmp)


q = deque()
for i in range(m):
    for j in range(n):
        for k in range(h):
            # z, y, x
            if arr[k][j][i] == 1:
                q.append((i, j, k))
# Start
bfs()

is_posssible = True
days_for_ripe = -1
for stairs in arr:
    for case in stairs:
        days_for_ripe = max(days_for_ripe, max(case))
        if 0 in case:
            print(-1)
            is_posssible = False
            break
    if not is_posssible:
        break
if is_posssible:
    print(days_for_ripe - 1)


# def bfs():
#     # 세로, 가로 이동
#     moves = [
#         [1, 0],
#         [-1, 0],
#         [0, 1],
#         [0, -1],
#         [n, 0],  # 위로 이동하려면 세로 길이만큼 플러스
#         [-n, 0]  # 아래로 이동하려면 세로 길이만큼 마이너스
#     ]
#     while q:
#         y, x = q.popleft()
#         for (dy, dx) in moves:
#             ny = y + dy
#             nx = x + dx
#             if 0 <= nx <= m-1 and 0 <= ny <= (n*h)-1:
#                 if arr[ny][nx] == 0:
#                     arr[ny][nx] = arr[y][x] + 1
#                     q.append((ny, nx))


# # 가로, 세로, 높이
# m, n, h = map(int, input().split())

# arr = []
# for _ in range(n*h):
#     arr.append(list(map(int, input().split())))

# q = deque()
# for i in range(n*h):
#     for j in range(m):
#         if arr[i][j] == 1:
#             q.append((i, j))
# # Start
# bfs()

# is_posssible = True
# days_for_ripe = -1
# for case in arr:
#     days_for_ripe = max(days_for_ripe, max(case))
#     if 0 in case:
#         print(-1)
#         is_posssible = False
#         break
# if is_posssible:
#     print(days_for_ripe - 1)
