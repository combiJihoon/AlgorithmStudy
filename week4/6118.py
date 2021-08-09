import sys
from collections import deque

input = sys.stdin.readline


def bfs():
    q = deque()
    q.append(1)
    visited[1] += 1
    while q:
        x = q.popleft()
        for i in arr[x]:
            if visited[i] == 0:
                visited[i] = visited[x] + 1
                q.append(i)


# 입력
n, m = map(int, input().split())

arr = [[] for _ in range(n+1)]
for _ in range(m):
    num, dist = map(int, input().split())
    arr[num].append(dist)
    arr[dist].append(num)

visited = [0] * (n+1)
bfs()
fartest_point = max(visited)
# 숨어야 하는 헛간 번호
for idx, value in enumerate(visited):
    if value == fartest_point:
        # value - 1 : 시작 지점 + 1 한 것 빼야 함!
        print(idx, value - 1, visited.count(fartest_point))
        break

'''
출력
숨어야 하는 헛간 번호, 그 헛간까지의 거리, 그 헛간과 같은 거리 갖는 헛간의 개수
거리가 같다면 헛간 번호 가장 작은 것을 출력하며,
거리가 같은 것의 개수도 함께 출력한다.
print(arr)
'''
