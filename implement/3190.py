import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
k = int(input())
arr = [[0] * n for _ in range(n)]
for _ in range(k):
    x, y = map(int, input().split())
    arr[x-1][y-1] = 1

dir_changes = dict()
l = int(input())
for _ in range(l):
    x, y = input().strip().split()
    dir_changes[int(x)] = y  # 해당 시간에 회전

# 북, 동, 남, 서(시계방향)
moves = [[-1, 0], [0, 1], [1, 0], [0, -1]]
d, t, nx, ny = 1, 0, 0, 0  # 초기 세팅값(초기 동쪽)


def turn(_d, d):
    if _d == 'D':  # 오른쪽
        d = (d+1) % 4
    else:  # 왼쪽
        d = (d-1) % 4
    return d


q = deque()  # 뱀의 위치
q.append((0, 0))  # 시작점
while True:
    t += 1
    dx = moves[d][0]
    dy = moves[d][1]
    nx += dx
    ny += dy

    # 시간이 되면 회전
    if t in dir_changes.keys():
        d = turn(dir_changes[t], d)
    if 0 <= nx <= n-1 and 0 <= ny <= n-1:
        if (nx, ny) in q:  # 자신에게 부딪침
            print(t)
            sys.exit()
        if arr[nx][ny] == 1:  # 사과 있으면 길이 증가
            arr[nx][ny] = 0
        else:
            x, y = q.popleft()  # 꼬리 자르기
        q.append((nx, ny))
    else:  # 벽에 부딪침
        print(t)
        sys.exit()
print(t)
