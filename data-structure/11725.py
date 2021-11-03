import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def find_parent(parent, parents):
    for child in nodes[parent]:
        if child != 1 and parents[child] == 0:
            parents[child] = parent
            find_parent(child, parents)


n = int(input())
nodes = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    nodes[a].append(b)
    nodes[b].append(a)

parents = [0] * (n+1)
find_parent(1, parents)

for parent in parents[2:]:
    print(parent)
