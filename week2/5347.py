'''1934 풀이와 동일'''

# 유클리드 호제법
# https: // tech.lonpeach.com/2017/11/12/Euclidean-algorithm/


def gcd(n, m):
    a = max(n, m)
    b = min(n, m)
    if a % b == 0:
        return b
    return gcd(b, a % b)


def minMul(n, m):
    maxDivisor = gcd(n, m)
    return (n // maxDivisor) * (m // maxDivisor) * maxDivisor


num = int(input())
for i in range(num):
    n, m = map(int, input().split())
    print(minMul(n, m))
