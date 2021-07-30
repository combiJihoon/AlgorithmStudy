import sys

input = sys.stdin.readline

n, m = map(int, input().split())
num_list = set(map(int, input().split()))
num_list = list(num_list)
num_list.sort()

stack = []
result = dict()
visited = [False] * len(num_list)


def dfs():
    if len(stack) == m:
        tmp = " ".join(map(str, stack))
        if tmp not in result:
            result[tmp] = True
            print(tmp)
            return

    for num in num_list:
        # 오름차순이어야 함
        if stack:
            if stack[-1] > num:
                continue
        stack.append(num)
        dfs()
        stack.pop()


dfs()
