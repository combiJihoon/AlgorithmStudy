import sys

input = sys.stdin.readline
n = int(input())
for _ in range(n):
    password = input().strip()

    left = []  # 커서의 왼쪽인 left에 일단 저장
    right = []
    for p in password:
        if p == '<':
            # left의 것을 빼고 left에 넣는다.(가장 왼쪽으로 가게 됨)
            if left:
                right.append(left.pop())
        elif p == '>':
            # right의 것을 빼고 right에 넣는다.(가장 오른쪽으로 가게 됨)
            if right:
                left.append(right.pop())
        elif p == '-':
            if left:
                left.pop()
        else:
            left.append(p)
    right = right[::-1]
    print("".join(left+right))

# 1
# j><>-<u->xb<<a
# axb
