import sys
import heapq

input = sys.stdin.readline
V, E = map(int, input().split())
k = int(input())  # start
arr = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    arr[u].append((w, v))

# heap에는 현재 노드에 연결된 노드를 넣는다.
# 이 때, 가장 가중치가 작은 노드부터 방문하기 위해 heap 사용
heap = []


def dijkstra(x):
    dp[x] = 0
    # (가중치, 노드)
    heapq.heappush(heap, (0, x))

    while heap:
        val, now = heapq.heappop(heap)
        # 이미 방문한 곳이므로 또 방문하지 않는다.
        if dp[now] < val:
            continue
        for new_val, nxt_node in arr[now]:
            nxt_val = val + new_val
            if nxt_val < dp[nxt_node]:
                dp[nxt_node] = nxt_val
                heapq.heappush(heap, (nxt_val, nxt_node))


dp = [int(1e9)] * (V+1)
dijkstra(k)

for i in range(1, V+1):
    print('INF' if dp[i] == int(1e9) else dp[i])
