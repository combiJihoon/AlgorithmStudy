import sys

input = sys.stdin.readline
n = int(input())
n_arr = sorted(list(map(int, input().split())))
m = int(input())
m_arr = list(map(int, input().split()))

'''
num_dict = {}
for num in n_arr:
    if num not in num_dict:
        num_dict[num] = 1
    else:
        num_dict[num] += 1

ans = [num_dict[val] if val in num_dict else 0 for val in m_arr]

print(*ans)
'''


def bs(s, e, t):
    if s > e:
        return 0

    mid = (s+e)//2
    if n_arr[mid] == t:
        return n_arr[s:e+1].count(t)
    elif n_arr[mid] < t:
        return bs(mid+1, e, t)
    else:
        return bs(s, mid-1, t)


_dict = {}
for i in m_arr:
    if i not in _dict:
        _dict[i] = bs(0, n-1, i)

ans = [_dict[val] if val in _dict else 0 for val in m_arr]
print(*ans)
