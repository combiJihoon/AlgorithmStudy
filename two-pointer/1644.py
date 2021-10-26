import sys

sys.setrecursionlimit(4000000)
input = sys.stdin.readline
n = int(input())


def prime_num(num):
    flags = [True] * (n+1)
    flags[0] = False
    flags[1] = False
    prime_nums = []

    for i in range(2, num+1):
        if flags[i]:
            prime_nums.append(i)
            for j in range(2*i, num+1, i):
                flags[j] = False

    return prime_nums


prime_nums = prime_num(n)
s = 0
e = 0
ans = 0

while e <= len(prime_nums) - 1:
    tmp = sum(prime_nums[s:e+1])
    if tmp == n:
        ans += 1
        e += 1
    elif tmp < n:
        e += 1
    else:
        s += 1

print(ans)
