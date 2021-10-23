import sys

input = sys.stdin.readline

n, m, l = map(int, input().split())
arr = list(map(int, input().split()))
arr.append(l)
arr = sorted(arr)


s = 1
e = l - 1

while s < e:
    mid = (s+e) // 2  # 휴게소들 사이의 간격

    cnt = 0  # 설치할 휴게소 개수
    cur = 0
    for point in arr:
        dist = point - cur
        cur = point
        if dist > mid:  # 간격이 mid보다 크면 휴게소 짓는다
            cnt += (dist - 1) // mid   # 사이에 지을 수 있는 개수(끝 점 제외이므로 -1)

    # cnt가 크다는 말은 설치한 간격이 좁다는 뜻이므로 넓혀야 한다.
    if cnt > m:
        s = mid + 1
    else:
        e = mid

print(e)
