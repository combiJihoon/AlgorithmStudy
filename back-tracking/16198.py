import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))


def collect_energy(arr):
    if len(arr) == 3:
        return arr[0] * arr[2]
    ans = -1
    for i in range(1, len(arr)-1):
        tmp = (arr[i-1]*arr[i+1]) + collect_energy(arr[:i] + arr[i+1:])
        ans = max(ans, tmp)
    return ans


print(collect_energy(arr))
