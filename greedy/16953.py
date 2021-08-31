import sys

input = sys.stdin.readline

a, b = map(int, input().split())


def sol(a, b):
    cnt = 0

    while True:
        if a == b:
            return cnt + 1
        elif a > b:
            return -1

        cnt += 1

        if str(b)[-1] == '1':
            b = int(str(b)[:-1])
        elif b % 2 == 0:
            b //= 2
        else:
            return -1


print(sol(a, b))
