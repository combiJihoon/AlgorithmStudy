import sys

input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(str(input().strip())))


def reversing(y, x):
    for i in range(y+1):
        for j in range(x+1):
            graph[i][j] = str(1 - int(graph[i][j]))


cnt = 0
for i in range(n-1, -1, -1):
    for j in range(m-1, -1, -1):
        if graph[i][j] == '1':
            cnt += 1
            reversing(i, j)
