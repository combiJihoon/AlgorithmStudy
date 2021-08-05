import sys
from itertools import permutations as pm

input = sys.stdin.readline

n = int(input())
signs = list(map(str, input().split()))

'''
백트래킹 : 잘 모르겠음...
def checkSign(a, b, sign):
    if sign == '<':
        return a < b
    if sign == '>':
        return a > b


max_str = ""
min_str = ""


def dfs(cnt, s):
    global min_str, max_str

    if cnt == n+1:
        if min_str > s:
            min_str = s
        if max_str < s:
            max_str = s
        return

    for i in range(10):
        if not visited[i]:
            if cnt == 0 or checkSign(int(s[-1]), i, signs[cnt-1]):
                visited[i] = True
                dfs(cnt+1, s+str(i))
                visited[i] = False


visited = [False] * 10
dfs(0, "")
print(max_str)
print(min_str)
'''

# 완전탐색: 시간초과
# pypy로 하면 통과됨

pm_nums = []
pm_nums += pm([i for i in range(10)], n+1)


def getSign(a, b):
    if a < b:
        return "<"
    else:
        return ">"


num_list = []
for nums in pm_nums:
    is_possible = True
    tmp = ""
    for i in range(1, len(nums)):
        a = nums[i-1]
        b = nums[i]
        if getSign(a, b) != signs[i-1]:
            is_possible = False
            break
        else:
            tmp += str(a)
    if is_possible:
        tmp += str(nums[len(nums)-1])
        num_list.append((int(tmp), tmp))

# 내림차순 정렬
num_list.sort(key=lambda x: -int(x[0]))
print(num_list[0][1])
print(num_list[len(num_list)-1][1])
