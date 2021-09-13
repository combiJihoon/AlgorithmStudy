import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]


def bfs(x, y, dp):
    q = deque()
    q.append((x, y))

    while q:
        x, y, val = q.popleft()
        for i in range(len(arr[y])):
            if dp[y][i] == 0:
                dp[x][y] = arr[y][i]
            else:
                dp[x][y] = min(dp[x][y], arr[y][i])


dp = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i != j:
            # 시작지점
            bfs(i, j, dp)

# print(ans)

# 여기까지 오는 최소 비용 구해 놓기
# 0이 아니라면 있는 값 쓰면 되고 0이라면 저장해 놓기
