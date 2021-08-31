'''
sorted 다중조건 적용하기
meetings = sorted(meetings, key=lambda x: (x[1], x[0]))
1번째 요소에 대하여 정렬 후 1번째 요소가 같을 경우 0번째 요소에 대하여 정렬한다.
1번째 요소에 대해서만 정렬할 경우 아래의 반례에 대해 해결하지 못한다.

5
4 4
4 4
3 4
2 4
1 4
meetings = [(4, 4), (4, 4), (1, 4), (2, 4), (3, 4)]  
정답은 3인데 2라는 오답이 나온다.
따라서 0번째 요소에 대해서도 정렬해 주어야 한다.
'''
import sys

input = sys.stdin.readline

n = int(input())

meetings = []
for _ in range(n):
    meetings.append(tuple(map(int, input().split())))

meetings = sorted(meetings, key=lambda x: (x[1], x[0]))

cnt = 1
start = meetings[0][0]
end = meetings[0][1]
for i in range(1, len(meetings)):
    if meetings[i][0] >= end:
        cnt += 1
        start = meetings[i][0]
        end = meetings[i][1]
print(cnt)
