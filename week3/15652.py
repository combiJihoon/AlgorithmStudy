import sys

input = sys.stdin.readline
n, m = map(int, input().split())

stack = []


def dfs():
    if len(stack) == m:
        # for i in range(1, len(stack)):
        #     if stack[i] < stack[i-1]:
        #         return
        print(" ".join(map(str, stack)))
        return

    for i in range(1, n+1):
        if stack and stack[-1] > i:
            continue
        else:
            stack.append(i)
            dfs()
            stack.pop()


dfs()
