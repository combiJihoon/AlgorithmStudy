'''
메모리를 조절하는 것이 중요한 문제
- max 값들을 저장할 max_dp를 생성
- max_dp에 바로 저장하면 다음 값은 이 전 값에 더해질 수 있으므로 'max_tmp'를 하나 더 생성한다.
'''
import sys

input = sys.stdin.readline

n = int(input())

max_dp = [0] * 3
min_dp = [0] * 3

max_tmp = [0] * 3
min_tmp = [0] * 3
for _ in range(n):
    x, y, z = map(int, input().split())
    for i in range(3):
        if i == 0:
            max_tmp[0] = x + max(max_dp[0], max_dp[1])
            min_tmp[0] = x + min(min_dp[0], min_dp[1])
        elif i == 1:
            max_tmp[1] = y + max(max_dp[0], max_dp[1], max_dp[2])
            min_tmp[1] = y + min(min_dp[0], min_dp[1], min_dp[2])
        else:
            max_tmp[2] = z + max(max_dp[1], max_dp[2])
            min_tmp[2] = z + min(min_dp[1], min_dp[2])

    for i in range(3):
        max_dp[i] = max_tmp[i]
        min_dp[i] = min_tmp[i]

print(max(max_dp), min(min_dp))
