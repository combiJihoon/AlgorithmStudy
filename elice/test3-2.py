import sys

input = sys.stdin.readline
# 숫자 개수, 플레이어 수, 선물 위치, 라운드의 수
n, k, p, l = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(k)]

player, rnd = -1, 1
cur = 1
is_winner = False
for i in range(l):  # l라운드
    for j in range(k):  # k명
        turn = arr[j][i]
        # 회전
        for _ in range(turn):
            if cur == 1:
                cur = n
            else:
                cur -= 1
        if cur == p:
            print(j+1, i+1)
            sys.exit()

print(-1)
