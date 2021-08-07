import sys
from itertools import permutations as pm

input = sys.stdin.readline

a, b = map(str, input().split())
b = int(b)
pm_a = list(pm(a, len(a)))


def digit_length(n):
    ans = 0

    while n:
        n //= 10
        ans += 1

    return ans


max_result = -1
for case in pm_a:
    tmp = int("".join(case))
    # C는 0부터 시작하면 안된다. 즉, 자릿수가 같아야 한다.
    if digit_length(int(tmp)) == len(a):
        if tmp < b:
            max_result = max(max_result, tmp)

print(max_result)
