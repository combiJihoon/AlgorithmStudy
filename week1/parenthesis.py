import sys

input = sys.stdin.readline
n = int(input())


def sol(paren):
    stack = []
    for p in paren:
        if p == "(":
            stack.append(p)
        else:
            if not stack:
                return "NO"
            else:
                stack.pop()
    if stack:
        return "NO"
    else:
        return "YES"


for i in range(n):
    paren = str(input()).strip()
    print(sol(paren))
