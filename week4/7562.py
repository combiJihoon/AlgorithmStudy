import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    moves = [
        [1, 2],
        [-1, 2],
        [2, 1],
        [2, -1],
        [1, -2],
        [-1, -2],
        [-2, 1],
        [-2, -1]
    ]

    q = deque()
    q.append((cur_y, cur_x))
    chess_arr[cur_y][cur_x] = 1

    while q:
        y, x = q.popleft()
        for (dy, dx) in moves:
            nx = x + dx
            ny = y + dy
            if 0 <= nx <= n-1 and 0 <= ny <= n-1:
                if chess_arr[ny][nx] == 0:
                    chess_arr[ny][nx] = chess_arr[y][x] + 1
                    if (nx, ny) == (t_x, t_y):
                        return
                    q.append((ny, nx))


tests = int(input())
for _ in range(tests):
    n = int(input())
    cur_x, cur_y = map(int, input().split())
    t_x, t_y = map(int, input().split())
    chess_arr = [[0] * n for _ in range(n)]
    # 시작부에 굳이 1 안해놔도 될듯...
    chess_arr[cur_y][cur_x] = 1
    bfs()
    tmp = chess_arr[t_y][t_x] - 1
    print(tmp)


'''
max_recursion_depth 오류 나옴
# max_recursion_depth 해결하는 코드 쓰면 됨
# sys.setrecursionlimit(10000)

def dfs(x, y, chess_arr):
    moves = [
        [1, 2],
        [-1, 2],
        [2, 1],
        [2, -1],
        [1, -2],
        [-1, -2],
        [-2, 1],
        [-2, -1]
    ]
    for i in range(8):
        dx, dy = moves[i]
        nx = x + dx
        ny = y + dy
        # 이동
        if 0 <= nx <= n-1 and 0 <= ny <= n-1:
            if chess_arr[ny][nx] == 0:
                chess_arr[ny][nx] = chess_arr[x][y] + 3
                if (nx, ny) == (t_x, t_y):
                    return
                dfs(nx, ny, chess_arr)
'''
