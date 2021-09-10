'''
https://hongcoding.tistory.com/50
d[n][k]는 N번째 물건 까지 살펴보았을 때, 무게가 K인 배낭의 최대 가치 이다
'''
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
things = [[0, 0]]
for _ in range(n):
    things.append(list(map(int, input().split())))
d = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        w = things[i][0]
        v = things[i][1]
        if j < w:
            # 새로 들어올 물건의 무게가 더 크다면 넣을 수 없다.
            d[i][j] = d[i-1][j]
        else:
            # 무게가 더 작은 것이 들어올 경우
            # j가 w보다 큰 경우 두 가지의 선택이 가능하다.
            # 1) 현재 넣을 물건의 무게만큼 배낭에서 빼고 현재 물건을 넣는다.
            # 2) 현재 물건을 넣지 않고 이전 배낭 그대로 가져간다.
            d[i][j] = max(d[i-1][j-w]+v, d[i-1][j])

print(d[n][k])


# w_and_v = [list(map(int, input().split())) for _ in range(n)]

# max_v = -1
# for i in range(len(w_and_v)):
#     cur_w = 0
#     w = w_and_v[i][0]
#     v = w_and_v[i][1]
#     if v > max_v:
#         max_v = v
#         cur_w = w
#     for j in range(i, -1, -1):
#         cur_w += w_and_v[j][0]
#         if w <= k:
#             if v + w_and_v[j][1] > max_v:
#                 max_v = v + w_and_v[j][1]
#             else:
#                 w -= w_and_v[j][0]
#         else:
#             cur_w = 0
#             break
# print(max_v)

# i = 1
# max_v = -1
# while i < n:
#     _cb = list(cb(w_and_v, n-i))
#     for case in _cb:
#         tmp_w = 0
#         tmp_v = 0
#         is_poss = True
#         for w, v in case:
#             tmp_w += w
#             tmp_v += v
#             if tmp_w > k:
#                 is_poss = False
#                 break
#         if is_poss:
#             max_v = max(max_v, tmp_v)
#     i += 1

# print(max_v)
