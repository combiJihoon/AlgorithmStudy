import sys

input = sys.stdin.readline
n = int(input())
length = len(str(n))

ans = 0
for i in range(1, length+1):
    if i == length:
        ans += i * (n - (10 ** (i-1)) + 1)
    else:
        ans += i * (9 * 10 ** (i-1))
print(ans)
