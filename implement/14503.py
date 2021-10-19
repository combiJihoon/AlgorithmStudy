import sys

input = sys.stdin.readline
n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]


# 북동남서 = 0123
# 현재 방향 + 3 % 4가 왼쪽 방향

ans = 0


def clean(x, y, d):
    global ans
    # 북, 동, 남, 서에 해당하는 인덱스의 이동
    moves = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    back = [2, 3, 0, 1]  # 후진 시에 사용하게 될 인덱스 별 moves 인덱스

    if arr[x][y] == 0:
        arr[x][y] = 2
        ans += 1
    # 4번 이동
    for _ in range(4):
        nd = (d + 3) % 4
        dx, dy = moves[nd]
        nx = x + dx
        ny = y + dy
        if arr[nx][ny] == 0:
            clean(nx, ny, nd)
            return
        d = nd
    # 모두 이동 끝나고 후진
    back = (d + 2) % 4  # 후진 위한 방향
    dx, dy = moves[back]
    nx = x + dx
    ny = y + dy
    if arr[nx][ny] == 1:
        return
    clean(nx, ny, d)


clean(r, c, d)
print(ans)
