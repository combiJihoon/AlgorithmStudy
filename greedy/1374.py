import sys
import heapq

input = sys.stdin.readline
n = int(input())
lectures = [tuple(map(int, input().split())) for _ in range(n)]
lectures = sorted(lectures, key=lambda x: x[1])
# 가장 빨리 시작하는 강의의 끝나는 시간
rooms = [lectures[0][2]]

for lecture in lectures[1:]:
    if rooms[0] > lecture[1]:
        heapq.heappush(rooms, lecture[2])
    else:
        heapq.heapreplace(rooms, lecture[2])

print(len(rooms))
