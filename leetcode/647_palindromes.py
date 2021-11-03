import sys

input = sys.stdin.readline

s = input().strip()


def substring(s, left, right):
    cnt = 0
    while left >= 0 and right < len(s):
        if s[left] != s[right]:
            break
        cnt += 1
        left -= 1
        right += 1

    return cnt


if len(s) == 1:
    print(1)
    sys.exit()
ans = 0
for i in range(len(s)):
    ans += substring(s, i, i)  # 홀수
    ans += substring(s, i, i+1)  # 짝수

print(ans)
