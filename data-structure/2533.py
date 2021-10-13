import sys

sys.setrecursionlimit(int(1e9))
input = sys.stdin.readline

n = int(input())
arr = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)


def dfs(x):
    v[x] = True
    dp[x][0] = 1  # 일단 x노드만 있다면 x노드 자신에 의해 adopted
    for i in arr[x]:
        if not v[i]:
            dfs(i)
            # 자식 노드가 얼리 어답터일 때와 아닐 때의 최솟값을 저장
            dp[x][0] += min(dp[i][0], dp[i][1])
            # 부모 노드가 얼리 어답터가 아니라면 자식 노드는 얼리 어답터야 한다.
            dp[x][1] += dp[i][0]


# dp[i][0]: i노드가 얼리 어답터일 때 서브트리에서 얼리 어답터의 최솟값
# dp[i][1]: i노드가 얼리 어답터가 아닐 때 서브트리에서 얼리 어답터의 최솟값
dp = [[0, 0] for _ in range(n+1)]
v = [False] * (n+1)

dfs(1)
# 값은 전부 부모노드에 저장되며, 가장 최상위 부모인 dp[1]을 출력한다.
print(min(dp[1][0], dp[1][1]))
