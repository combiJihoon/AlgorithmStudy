import sys

input = sys.stdin.readline

n = int(input())


def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == (x - i):
            return False
    return True


ans = 0


def n_queens(depth):
    global ans

    if depth == n:
        ans += 1

    else:
        for i in range(n):
            row[depth] = i
            if is_promising(depth):
                n_queens(depth+1)


# 모든 행마다 퀸이 있어야 하며 열이 겹치지 않아야 한다.
row = [0] * n
# 0번째 행부터 시작
n_queens(0)
print(ans)
