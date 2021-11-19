import sys

input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().strip())) for _ in range(n)]


def sol(x, y, n):
    if n == 1:
        return str(arr[x][y])

    ans = []
    for i in range(x, x+n):
        for j in range(y, y+n):
            if arr[i][j] != arr[x][y]:  # 다르면 사분면 분할
                ans.append('(')
                ans.extend(sol(x, y, n // 2))
                ans.extend(sol(x, y + n // 2, n // 2))
                ans.extend(sol(x + n // 2, y, n // 2))
                ans.extend(sol(x + n // 2, y + n // 2, n // 2))
                ans.append(')')
                return ans

    return str(arr[x][y])


print("".join(sol(0, 0, n)))
