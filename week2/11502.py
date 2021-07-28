import sys
# from itertools import product

input = sys.stdin.readline
t = int(input())
t_list = []
for _ in range(t):
    t_list.append(int(input()))

'''
1. 소수 찾기
2. x <= 1000 인 소수 x 구하기
3. 3개의 조합 만들기
4. k가 되는지 확인하기
5. 되면 오름차순 정렬/ 안되면 0
'''

'''
시간 초과
def findPrime(t):
    prime_candidates = []
    primes = [True] * (t-1)
    for i in range(2, (t-1)):
        if primes[i]:
            prime_candidates.append(i)
            j = 2*i
            while j < (t-1):
                primes[j] = False
                j += i

    # for i in range(2, len(primes)):
    #     if primes[i]:
    #         prime_candidates.append(i)

    prime_product = []
    prime_product += product(prime_candidates, repeat=3)

    for primes in prime_product:
        tmp = 0
        x, y, z = primes
        tmp = x + y + z

        if tmp == t:
            return primes

    return 0


# t_list의 해당 원소까지만 소수 구하기
for t in t_list:
    print(*findPrime(t))
'''


# def isPrime(a):
#     if a == 2:
#         return True
#     for i in range(2, a):
#         if a % i == 0:
#             return False
#     return True

def findPrime(t):
    prime_candidates = []
    primes = [True] * (t-1)
    for i in range(2, (t-1)):
        if primes[i]:
            prime_candidates.append(i)
            j = 2*i
            while j < (t-1):
                primes[j] = False
                j += i
    return prime_candidates


def sol(prime_candidates, t):
    for i in prime_candidates:
        for j in prime_candidates:
            for k in prime_candidates:
                if i + j + k == t:
                    return i, j, k
    return 0


for t in t_list:
    prime_candidates = findPrime(t)
    print(*sol(prime_candidates, t))
