import sys
import heapq

input = sys.stdin.readline
n = int(input())
arr = [int(input()) for _ in range(n)]

# 중앙값 기준으로 작은거 왼쪽, 큰거 오른쪽
s = []
b = []
cnt = 0
mid = -1
for i in arr:
    cnt += 1
    if i > mid:
        heapq.heappush(b, i)
    else:
        heapq.heappush(s, -i)

    if (len(b) < len(s) and len(b) != len(s) + 1) or (len(b) > len(s) and len(b) != len(s) + 1):
        if len(b) > len(s):
            x = heapq.heappop(b)
            heapq.heappush(s, -x)
        else:
            x = heapq.heappop(s)
            heapq.heappush(b, -x)
    if cnt % 2 == 0:
        mid = min(-s[0], b[0])
    else:
        mid = b[0]
    print(mid)

# [1, 5, 2, 10, -99, 7, 5]
# s = [-2, -1, 99]
# b = [5, 5, 7, 10]
# mid = 1, 1, 2, 2, 2
# cnt = 1
# b의 길이가 크면 s에 넣는다.
# b의 길이가 1개 더 크도록 만든다.(이동)
# s[0]을 이동시킨다.


# [-11, -10, 4]
# 4
# -10, -11, 4, 5
# -10,
# s = [-11]
# b = [-10, -4]
# -10, -11, -10, -11
