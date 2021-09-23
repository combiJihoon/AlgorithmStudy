import sys
from itertools import combinations as cb

sys.setrecursionlimit(1000)
input = sys.stdin.readline

# 세로, 가로
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 벽을 세워보고
# 퍼뜨리고
# 안전영역 크기 구하기

safe_area = 0


def dfs(x, y, new_arr):

    moves = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    for dx, dy in moves:
        nx = x + dx
        ny = y + dy
        if 0 <= nx <= n-1 and 0 <= ny <= m-1:
            if new_arr[nx][ny] == 0:
                new_arr[nx][ny] = 2
                dfs(nx, ny, new_arr)


def spread():
    global safe_area
    # arr를 visited에 복사
    # 1, 2, 0 세 가지로 표현되기 때문에 구분위해 복사
    new_arr = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            new_arr[i][j] += arr[i][j]

    for i in range(n):
        for j in range(m):
            # 2가 나오면 퍼뜨리기 시작
            if arr[i][j] == 2:
                dfs(i, j, new_arr)

    # 최댓값 구하기
    tmp = 0
    for case in new_arr:
        tmp += case.count(0)

    safe_area = max(safe_area, tmp)


def build_walls():
    # 벽 세우기
    # 0인 좌표를 모아서 cb
    no_walls = []
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                no_walls.append((i, j))
    cb_walls = list(cb(no_walls, 3))
    for case in cb_walls:
        # 벽 세우기
        for x, y in case:
            arr[x][y] += 1
        # 퍼뜨리고 안전영역 최댓값 구하기
        spread()
        # 벽 지우기
        for x, y in case:
            arr[x][y] -= 1


build_walls()
print(safe_area)
