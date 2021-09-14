import sys
import heapq

input = sys.stdin.readline

n = int(input())
lectures = sorted([tuple(map(int, input().split())) for _ in range(n)])
rooms = [lectures[0][1]]

for lecture in lectures[1:]:
    if rooms[0] > lecture[0]:
        heapq.heappush(rooms, lecture[1])
    else:
        heapq.heapreplace(rooms, lecture[1])

print(len(rooms))
