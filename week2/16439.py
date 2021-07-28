import sys
from itertools import combinations as cb

input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))


# 한 사람의 만족도는 시킨 치킨 중에서 선호도가 가장 큰 값
# 행에서도 최대, 열에서도 최대가 되어야 함
# 3가지 까지 고른다.

# 치킨 3종류 고르기(인덱스 : 0~4)
chickens = [i for i in range(m)]

final_satisfaction = 0
how_many = 3
while how_many > 0:
    nums = []
    nums += cb(chickens, how_many)

    satisfaction = 0
    for num in nums:  # (0, 3, 4)
        tmp = 0
        for person in arr:  # [1,2,3,4,5]
            max_preference = -1
            for n in num:  # n = 0, 3, 4
                max_preference = max(max_preference, person[n])
            tmp += max_preference
        satisfaction = max(satisfaction, tmp)
    final_satisfaction = max(final_satisfaction, satisfaction)
    how_many -= 1

print(final_satisfaction)
