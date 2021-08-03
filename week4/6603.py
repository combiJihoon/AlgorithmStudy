import sys
from itertools import combinations as cb

input = sys.stdin.readline

test_cases = []
while True:
    case = list(map(int, input().split()))
    if case == [0]:
        break
    else:
        test_cases.append(case)


for case in test_cases:
    new_case = case[1:]
    cb_new_case = []
    cb_new_case += cb(new_case, 6)
    for i in cb_new_case:
        print(*i)
    print()
