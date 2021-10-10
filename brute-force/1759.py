import sys
import string
from itertools import combinations as cb

input = sys.stdin.readline
L, C = map(int, input().split())
arr = list(map(str, input().strip().split()))

vow = list("aeiou")  # 모음
con = [i for i in string.ascii_lowercase if i not in vow]  # 자음

vow_arr = [i for i in arr if i in vow]
con_arr = [i for i in arr if i in con]


ans = []
i = 1
j = 2
for i in range(1, L):
    vow_cb = list(cb(vow_arr, i))
    for case_vow in vow_cb:
        j = L - i
        if j >= 2:  # 자음 2개 이상
            con_cb = list(cb(con_arr, j))
            for case_con in con_cb:
                ans.append("".join(sorted((case_vow+case_con))))

for i in sorted(ans):
    print(i)
