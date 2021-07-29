import sys
from itertools import combinations as cb

INF = int(1e9)
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))


# 능력치 구하기 위해 필요한 함수들
def pickTwo(_list):
    cb_list = list(cb(_list, 2))
    return cb_list


def getPower(cb_list):
    power_sum = 0
    for case in cb_list:
        x, y = case
        power = arr[x-1][y-1] + arr[y-1][x-1]
        power_sum += power
    return power_sum


def getPowerDifference(power1, power2):
    difference = abs(power1 - power2)
    return difference


teams = list(cb([i for i in range(1, n+1)], n//2))

# Start
min_difference = INF
for team in teams:
    visited = [False] * (n+1)
    for ppl in team:
        visited[ppl] = True
    the_other_team = [i for i in range(1, n+1) if not visited[i]]

    team = pickTwo(team)
    the_other_team = pickTwo(the_other_team)

    power1 = getPower(team)
    power2 = getPower(the_other_team)

    power_difference = getPowerDifference(power1, power2)

    min_difference = min(min_difference, power_difference)


print(min_difference)

'''
1~n 중에서 2개를 뽑는다. -> 그러면 나머지가 다른 팀이 된다.
arr에서 팀의 능력치를 각각 구하고 차이를 구한다.
차이가 최소가 되도록 한다.
'''
