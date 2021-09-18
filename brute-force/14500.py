import sys

input = sys.stdin.readline
n, m = map(int, input().split())  # 행, 열
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

max_val = max(map(max, arr))
ans = -1


def dfs(x, y, val, cnt):
    global max_val
    global ans

    moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    if cnt == 4:
        ans = max(ans, val)
    # max_val 값이 하나라도 들어가지 않으면 최대가 될 수 없다.
    if val + max_val * (4-cnt) < ans:
        return
    for dx, dy in moves:
        nx = x + dx
        ny = y + dy
        if 0 <= nx <= n-1 and 0 <= ny <= m-1:
            if not visited[nx][ny]:
                visited[nx][ny] = True
                if cnt == 2:
                    # ㅗ 모양 처리: 이동하지 않고 값만 더한다.
                    dfs(x, y, val+arr[nx][ny], cnt+1)
                # 위와 동시에 이동하는 경우도 처리한다.
                dfs(nx, ny, val+arr[nx][ny], cnt+1)
                visited[nx][ny] = False


visited = [[False] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, arr[i][j], 1)
        visited[i][j] = False


print(ans)
