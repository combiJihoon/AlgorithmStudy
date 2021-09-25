import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

shark = 2
# 상어 찾기
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            new_x, new_y = i, j
            arr[new_x][new_y] = 0


def bfs():
    dist = [[-1]*n for _ in range(n)]
    dist[new_x][new_y] = 0
    q = deque()
    q.append((new_x, new_y))
    # top -> left -> bottom -> right
    moves = [[-1, 0], [0, -1], [1, 0], [0, 1]]
    while q:
        x, y = q.popleft()
        for dx, dy in moves:
            nx = x + dx
            ny = y + dy
            if 0 <= nx <= n-1 and 0 <= ny <= n-1:
                if dist[nx][ny] == -1:
                    if arr[nx][ny] <= shark:
                        dist[nx][ny] = dist[x][y] + 1
                        q.append((nx, ny))

    return dist


def find_fish(dist):
    x = 0
    y = 0
    min_dist = int(1e9)
    for i in range(n):
        for j in range(n):
            if dist[i][j] != -1 and 0 < arr[i][j] < shark:
                if min_dist > dist[i][j]:
                    min_dist = dist[i][j]
                    x, y = i, j  # 상어 자리 이동

    if min_dist == int(1e9):
        return None
    else:
        return x, y, min_dist


ans = 0
eaten = 0
while True:
    val = find_fish(bfs())
    if val is None:  # 더 이상 먹을 물고기 없음
        print(ans)
        break
    else:
        new_x, new_y = val[0], val[1]
        ans += val[2]
        arr[new_x][new_y] = 0  # 먹었으니까 0
        eaten += 1
        if eaten == shark:
            shark += 1
            eaten = 0
