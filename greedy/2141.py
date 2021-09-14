import sys

sys.setrecursionlimit(2000)
input = sys.stdin.readline

n = int(input())

# [위치, 사람 수]
arr = []
total_ppl = 0
for _ in range(n):
    pos, ppl = map(int, input().split())
    total_ppl += ppl
    arr.append((pos, ppl))

# 위치 순서대로 정렬
arr = sorted(arr, key=lambda x: x[0])
# 버림이 아닌 반올림을 해야 한다.
mid = round(total_ppl / 2)
cnt = 0
for pos, ppl in arr:
    cnt += ppl
    if cnt >= mid:
        print(pos)
        break


# 사람이 많은 곳으로부터의 거리를 늘리면서 확인한다.
# pos = 0
# dist = int(1e9)
# for point in x:
#     tmp = 0
#     for i in range(n):
#         tmp += a[i] * abs(x[i]-point)
#     if tmp < dist:
#         dist = tmp
#         pos = point

# print(pos)
