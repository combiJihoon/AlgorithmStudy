import sys
import heapq

input = sys.stdin.readline

# 최소 비교 횟수 구하기
n = int(input())
cards = sorted([int(input()) for _ in range(n)])

if n == 1:
    print(0)
else:
    save = 0
    while len(cards) != 1:
        x = heapq.heappop(cards)
        y = heapq.heappop(cards)
        heapq.heappush(cards, x+y)
        save += (x+y)

    print(save)

# stack = [70, 120, 220]
# hq = [100, 120]
# 4
# 30
# 40
# 50
# 100
# 답 410


# stack = [70, 110, 180] = 360
# hq = [70, 110]
# 4
# 30
# 40
# 50
# 60
# 답 360
