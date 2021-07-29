import sys

input = sys.stdin.readline

n, m = map(int, input().split())

stack = []


def dfs():
    if len(stack) == m:
        if m == 1:
            print(" ".join(map(str, stack)))
            return
        else:
            for i in range(1, len(stack)):
                # 작은 인덱스의 요소가 더 작으면 print 안하고 return
                if stack[i] < stack[i-1]:
                    return
            print(" ".join(map(str, stack)))
            return

    for i in range(1, n+1):
        if i not in stack:
            stack.append(i)
            dfs()
            stack.pop()


dfs()
