import sys

input = sys.stdin.readline


def dfs(root, water_list, visited):
    stack = [root]  # 가장 처음 가진 물
    visited[root] = True

    while stack:
        start = stack.pop()
        water = water_list[start]

        cnt = 0
        for v in arr[start]:  # start와 연결된 노드
            if not visited[v]:
                cnt += 1  # 연결된 노드에 같은 확률로 물을 줘야 하므로 갯수 세기

        if cnt == 0:
            continue
        val = water / cnt
        water_list[start] = 0  # 물을 다 줬으므로 0

        for v in arr[start]:
            if not visited[v]:
                stack.append(v)  # 물을 받은 다른 자식 노드들이 stack에 추가됨
                visited[v] = True
                water_list[v] += val


n, w = map(int, input().split())
arr = [[] for _ in range(n+1)]
for _ in range(n-1):
    x, y = map(int, input().split())
    arr[x].append(y)
    arr[y].append(x)
water = [0] * (n+1)
water[1] = w

visited = [False] * (n+1)
dfs(1, water, visited)

ans, cnt = 0, 0
for i in water:
    if i != 0:
        ans += i
        cnt += 1

print(round(ans/cnt, 10))
