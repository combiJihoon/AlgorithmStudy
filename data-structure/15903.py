import sys
import heapq

input = sys.stdin.readline
n, m = map(int, input().split())
cards = list(map(int, input().split()))
heapq.heapify(cards)

while m > 0:
    x = heapq.heappop(cards)
    y = heapq.heappop(cards)

    for _ in range(2):
        heapq.heappush(cards, x+y)

    m -= 1

print(sum(cards))
