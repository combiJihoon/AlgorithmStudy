import sys
from collections import deque

# sys.setrecursionlimit(100000)
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(n)]

# 가는 길에 1이 있다면 하나 부수고 이동 가능한지 확인
# 1 다음 칸이 0이라면 부수도록 한다.


def bfs():
    q = deque()
    visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
    visited[0][0][1] = 1
    # x, y, destroy_cnt(1이면 부술 수 있다. 0이면 없다.)
    q.append((0, 0, 1))

    moves = [[-1, 0], [1, 0], [0, 1], [0, -1]]
    while q:
        x, y, destroy_cnt = q.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y][destroy_cnt]
        for dx, dy in moves:
            nx = x + dx
            ny = y + dy
            if 0 <= nx <= n-1 and 0 <= ny <= m-1:
                if arr[nx][ny] == 0 and visited[nx][ny][destroy_cnt] == 0:
                    q.append((nx, ny, destroy_cnt))
                    visited[nx][ny][destroy_cnt] = visited[x][y][destroy_cnt] + 1
                if arr[nx][ny] == 1 and destroy_cnt == 1:
                    # 한 번 부수면 이제 부술 수 없으므로 destroy_cnt = 0
                    q.append((nx, ny, 0))
                    visited[nx][ny][0] = visited[x][y][1] + 1
    return -1


print(bfs())

# 5 5
# 00000
# 11101
# 00001
# 01111
# 00010

# 5 8
# 01000000
# 01010000
# 01010000
# 01010011
# 00010010
