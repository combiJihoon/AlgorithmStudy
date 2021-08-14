import sys

input = sys.stdin.readline

n, k = map(int, input().split())

sum_min = k * (k+1) // 2
if sum_min > n:
    print(-1)
elif (n - sum_min) % k == 0:
    print(k-1)
else:
    print(k)


'''
cb_list = list(cb([i for i in range(1, n+1)], k))
min_diff = int(1e9)
is_possible = True
for case in cb_list:
    if sum(case) == n:
        diff = case[-1] - case[0]
        if diff == 0:
            print(-1)
            is_possible = False
            break
        min_diff = min(min_diff, diff)
    elif sum(case) > n:
        break

print(min_diff if min_diff < int(1e9) else -1)
'''
