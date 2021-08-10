import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    moves = [
        [1, 0],
        [-1, 0],
        [0, 1],
        [0, -1]
    ]

    while q:
        y, x = q.popleft()
        for (dy, dx) in moves:
            ny = y + dy
            nx = x + dx
            if 0 <= ny <= n-1 and 0 <= nx <= m-1:
                if arr[ny][nx] == 0:
                    arr[ny][nx] = arr[y][x] + 1
                    # arr[ny][nx] = 2
                    q.append((ny, nx))


# m : 가로, n:세로
m, n = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

q = deque()
for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append((i, j))

bfs()

is_possible = True
days_for_ripe = -1
for case in arr:
    if 0 in case:
        print(-1)
        is_possible = False
        break
    else:
        days_for_ripe = max(days_for_ripe, max(case))

if is_possible:
    print(days_for_ripe - 1)

# print(arr)


'''
1일 경우 매일 동시에 퍼져야 하기 때문에 
1이 나오면 queue에 넣어서 arr 변화를 주어야 한다.
-> 이전 값보다 +1을 해준다.
'''
