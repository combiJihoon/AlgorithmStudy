import sys

input = sys.stdin.readline
n = int(input())
k = int(input())


def b_s(s, e, t):
    while s <= e:
        mid = (s+e) // 2

        # mid보다 작은 수들의 개수 구하기
        # 즉, mid가 몇 번째 수인지 구하는 것이 됨
        cnt = 0
        for i in range(1, n+1):
            cnt += min(mid//i, n)

        if cnt >= t:
            e = mid - 1
        else:
            s = mid + 1

    return s


print(b_s(0, n*n, k))


# 1 2 3
# 2 4 6
# 3 6 9
# 4 8 12

# 1 2 3 2 4 6 3 6 9
# 1 2 2 3 3 4 6 6 9

# k를 n으로 나눈 몫: 2
# k를 n으로 나눈 나머지: 1
# 2행 1열
