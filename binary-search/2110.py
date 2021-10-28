import sys

input = sys.stdin.readline
n, c = map(int, input().split())
arr = sorted([int(input()) for _ in range(n)])

ans = -1
s = 1
e = arr[-1] - arr[0]

while s <= e:
    mid = (s + e) // 2  # 공유기 사이의 거리

    cur = arr[0]
    cnt = 1  # cur 설치 했음
    for i in range(1, len(arr)):
        if arr[i] >= cur + mid:  # 공유기 사이 거리의 최소 이상이면 설치
            cnt += 1
            cur = arr[i]

    if cnt >= c:  # c보다 개수가 많으면 거리를 넓히기
        ans = mid
        s = mid + 1
    else:
        e = mid - 1

print(ans)
