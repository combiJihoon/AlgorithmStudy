import sys

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    # 정렬한 값 중 인덱스가 2 떨어져 있는 것들 중 차이가 가장 큰 값이 최소가 되도록 해야 함
    # 인접한 것 끼리는 가장 차이가 작은 것이기 때문에 2 차이가 날 경우 차이가 가장 작으면 된다.
    arr = sorted(list(map(int, input().split())))

    ans = -1
    for i in range(2, n):
        ans = max(ans, arr[i]-arr[i-2])
    print(ans)
