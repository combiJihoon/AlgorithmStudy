# pypy로 해결

import sys

input = sys.stdin.readline


def dfs(x, y, visited):
    # 상, 하, 좌, 우, 대각선
    move = [
        [0, -1],
        [0, 1],
        [-1, 0],
        [1, 0],
        [1, 1],
        [1, -1],
        [-1, 1],
        [-1, -1]
    ]

    for i in range(8):
        dx, dy = move[i]
        nx = x + dx
        ny = y + dy

        if 0 <= nx <= w-1 and 0 <= ny <= h-1:
            if visited[ny][nx] == 0:
                visited[ny][nx] = 1
                if arr[ny][nx] == 1:
                    dfs(nx, ny, visited)


result = []
# 입력
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    arr = []
    for _ in range(h):
        arr.append(list(map(int, input().split())))

    cnt = 0
    visited = [[0] * w for _ in range(h)]
    for i in range(w):
        for j in range(h):
            if arr[j][i] == 1 and visited[j][i] == 0:
                dfs(i, j, visited)
                cnt += 1

    result.append(cnt)

for cnt in result:
    print(cnt, end="\n")
