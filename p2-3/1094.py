import sys

input = sys.stdin.readline
print(bin(int(input())).count("1"))


'''
# 그대로 구현한 풀이
import sys
import heapq

input = sys.stdin.readline
x = int(input())
sticks = [64]

if x == sum(sticks):
    print(1)
else:
    # 당연히 합이 64보다 작겠지만...
    while sum(sticks) <= 64:
        stick = heapq.heappop(sticks)
        half_stick = stick // 2
        if sum(sticks) + half_stick == x:
            # 남은 stick과 half_stick의 개수 더해서 출력
            print(len(sticks)+1)
            break
        # sticks의 합과 half_stick의 합이 x보다 크면 half_stick만 push
        elif sum(sticks) + half_stick > x:
            heapq.heappush(sticks, half_stick)
        # sticks의 합과 half_stick의 합이 x보다 작다면 half_stick 둘 다 push
        else:
            heapq.heappush(sticks, half_stick)
            heapq.heappush(sticks, half_stick)
'''
