import sys
from collections import deque

input = sys.stdin.readline


def bfs(arr, x, y, val):
    q = deque()
    q.append((x, y))
    moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    while q:
        x, y = q.popleft()
        for dx, dy in moves:
            nx = x + dx
            ny = y + dy
            if 0 <= nx <= n-1 and 0 <= ny <= n-1:
                if arr[nx][ny] == val:
                    # 값이 같은 곳은 0으로 만들며 전부 방문
                    arr[nx][ny] = 0
                    q.append((nx, ny))


n = int(input())
norm = [list(input().strip()) for _ in range(n)]
weak = [[0]*n for _ in range(n)]
# 적록색약용: R, G는 같은 값으로 표기
for i in range(n):
    for j in range(n):
        if norm[i][j] == 'R' or norm[i][j] == 'G':
            weak[i][j] = 'R'
        else:
            weak[i][j] = 'B'

norm_cnt = 0
weak_cnt = 0
for i in range(n):
    for j in range(n):
        # 갔던 곳은 0이 되며 0이 아닌 경우 새롭게 방문한다.
        if norm[i][j] != 0:
            # 새롭게 방문시 cnt 1 증가
            norm_cnt += 1
            bfs(norm, i, j, norm[i][j])
        if weak[i][j] != 0:
            weak_cnt += 1
            bfs(weak, i, j, weak[i][j])
print(norm_cnt, weak_cnt)
