import sys

input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

# 오른쪽, 아래로만 점프 가능
# 나한테는 왼쪽, 위에서만 옴
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for x in range(n):
    for y in range(n):
        if x == n-1 and y == n-1:
            print(dp[x][y])
            break
        cur = arr[x][y]
        # 오른쪽
        if y + cur < n:
            dp[x][y + cur] += dp[x][y]
        # 아래
        if x + cur < n:
            dp[x+cur][y] += dp[x][y]
