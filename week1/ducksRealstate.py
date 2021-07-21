import sys
from collections import deque

input = sys.stdin.readline


# [[], [2, 3], [4, 5], [6]]

def duckHouse(house, qualified):
    visited = [0] * (n+1)
    q = deque()
    q.append(1)

    while q:
        x = q.popleft()
        visited[x] = 1

        for i in territory[x]:
            if visited[i] == 0:
                visited[i] = 1
                if qualified[i] == True:
                    return i
                elif qualified[i] == False and i == house:
                    qualified[house] = True
                    return 0
                else:
                    q.append(i)
            print(visited)


n, m = map(int, input().split())

# territory 채우기
territory = [[]]
i = 1
while True:
    temp = []
    left = 2*i
    right = 2*i + 1
    if left < (n+1):
        temp.append(left)
    if right < (n+1):
        temp.append(right)
    territory.append(temp)

    if left > n or right > n:
        break
    else:
        i += 1

qualified = [False]*(n+1)

for i in range(m):
    house = int(input())
    print(duckHouse(house, qualified))
