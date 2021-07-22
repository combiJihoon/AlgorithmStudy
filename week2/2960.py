import sys

input = sys.stdin.readline


def isPrime(num):
    is_prime = False
    cnt = 0
    for i in range(2, num+1):
        if num % i == 0:
            cnt += 1
            if cnt > 1:
                break
    if cnt == 1:  # i가 소수
        is_prime = True  # 소수임을 표시
        return is_prime


n, k = map(int, input().split())

removed = [False] * (n+1)
result = 0

for i in range(2, n+1):
    if isPrime(i):
        # 소수 제거
        j = 1
        while i*j <= n:
            if removed[i*j] == False:
                removed[i*j] = True
                result += 1
                if result == k:
                    print(i*j)
                    break
            j += 1

'''
1) 7 -> 2, 3, 4, 5, 6, 7
2) p(=2)의 배수 지우기 -> 2, 4, 6 지우기
    = > 남은 수 : 3, 5, 7 
2-1) p(=3)의 배수 지우기 -> 3 지우기
    => 남은 수 : 5, 7 
2-2) p(=5)의 배수 지우기 -> 5 지우기
    => 남은 수 : 7
'''
