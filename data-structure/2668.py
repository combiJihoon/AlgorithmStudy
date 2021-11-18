import sys


def dfs(v, i):
    visited[v] = True
    for val in arr[v]:
        if not visited[val]:
            dfs(val, i)
        elif visited[val] and val == i:  # 사이클이 생기면 append
            ans.append(val)


input = sys.stdin.readline
n = int(input())
arr = [[] for _ in range(n+1)]
for i in range(n):
    arr[i+1].append(int(input()))

ans = []
for i in range(1, n+1):
    visited = [False] * (n+1)
    dfs(i, i)


print(len(ans))
print(*sorted(ans), sep='\n')
