import sys

input = sys.stdin.readline
n = int(input())
k = int(input())  # 최대 k개의 집중국 설치 가능
sensors = sorted(list(map(int, input().split())))

# k개를 지으니까 최대 k-1개의 기준으로 나눈다.
# 가장 큰 거리를 최대 k번 지워나가며 거리의 합의 최솟값을 찾는다.
dist = []
for i in range(1, len(sensors)):
    dist.append(sensors[i]-sensors[i-1])

dist = sorted(dist, reverse=True)
ans = int(1e9)
idx = 0
while k > 0:
    ans = min(ans, sum(dist[idx:]))
    k -= 1
    idx += 1

print(ans)
