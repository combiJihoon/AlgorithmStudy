import sys
from itertools import combinations as cb

input = sys.stdin.readline

n, s = map(int, input().split())
s_list = list(map(int, input().split()))

'''
크기가 양수인 부분수열 중 다 더한 값이 s가 되는 경우의 수
'''
# cnt = 0
# for i in range(len(_list)):
#     tmp_sum = _list[i]
#     for j in range(i+1, len(_list)):
#         tmp_sum += _list[j]
#         if tmp_sum == s:
#             cnt += 1

# return cnt


def getSum(_list):
    cnt = 0
    for case in _list:
        tmp = sum(case)
        if tmp == s:
            cnt += 1

    return cnt


result = 0
size = n
while size > 0:
    cb_s_list = []
    cb_s_list += cb(s_list, size)
    result += getSum(cb_s_list)
    size -= 1

print(result)
