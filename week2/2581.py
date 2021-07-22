import sys

input = sys.stdin.readline

m = int(input())
n = int(input())
INF = int(1e9)

min_result = INF
sum_result = 0
has_prime = False

for i in range(m, n+1):
    cnt = 0
    for j in range(2, i+1):
        if i % j == 0:
            cnt += 1
            if cnt > 1:
                break
    if cnt == 1:  # i가 소수
        has_prime = True  # 소수임을 표시
        min_result = min(min_result, i)
        sum_result += i

# 소수가 없는 경우
if not has_prime:
    print(-1)
else:
    print(sum_result)
    print(min_result)


# 약수의 개수 구하기
# 약수 개수 2개면 소수
