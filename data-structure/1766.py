import sys
import heapq

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [[] for _ in range(n+1)]
precedes = [0] * (n+1)

heap = []  # 선행 문제가 없는 문제들 보관
ans = []  # 다 푼 문제들 보관
for _ in range(m):
    x, y = map(int, input().split())
    # x 뒤에 y 온다.
    arr[x].append(y)
    # y보다 먼저 오는 것의 갯수 추가
    precedes[y] += 1

for i in range(1, n+1):
    # 선행하는 것이 없다.(뒤에 오는 것만 있다.)
    if precedes[i] == 0:
        heapq.heappush(heap, i)

# 선행 문제가 남아 있는 나머지 문제들 해결
while heap:
    num = heapq.heappop(heap)
    ans.append(num)
    # num을 푼 다음에 풀 수 있는 문제들 확인한다.
    for i in arr[num]:
        # 선행 문제인 num을 풀었으므로 -1 해준다.
        precedes[i] -= 1
        if precedes[i] == 0:
            # 선행 문제가 더 이상 없으므로 heap에 넣는다.
            heapq.heappush(heap, i)

print(*ans)
