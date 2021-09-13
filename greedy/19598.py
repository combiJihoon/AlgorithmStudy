# https://deok2kim.tistory.com/m/324
import sys
import heapq

input = sys.stdin.readline
n = int(input())

arr = sorted([tuple(map(int, input().split())) for _ in range(n)])
# 가장 빨리 시작하는 것의 끝나는 시간
rooms = [arr[0][1]]
for meeting in arr[1:]:
    # 예약된 회의(rooms[0])의 끝나는 시간이 대기중인 회의(meeting[0]) 시작 시간보다 늦는 경우
    if rooms[0] > meeting[0]:
        # rooms에 추가시 rooms의 개수가 늘어난다.(즉, 다른 회의실이 열린다.)
        heapq.heappush(rooms, meeting[1])
    else:
        # heapreplace는 가장 작은 요소 빼고 추가할 요소 넣는다.
        # 한 회의실만 사용하게 되기 때문에 마지막 meeting 끝나는 시간만을 넣는다.
        heapq.heapreplace(rooms, meeting[1])

print(len(rooms))

'''
1: [0, 40]
2: [5, 10], [15, 30]
# 반례
3
0 10
5 20
15 25
1: 5 20
2: 0 10, 15 25
# 답 2

'''
